"""
logging_config.py
=================

One place to set up logging for the whole program.

HOW TO USE
----------
In every script you RUN directly (an "entry point"), call setup_logging() once,
as the very first thing inside the `if __name__ == "__main__":` block:

    from logging_config import setup_logging

    if __name__ == "__main__":
        setup_logging()
        ...

In every OTHER file (library files like base.py), never configure logging.
Only create a logger and use it:

    import logging
    logger = logging.getLogger(__name__)
    logger.info("Something happened")

THE MENTAL MODEL (read this when you forget)
--------------------------------------------
1. A log call creates a LogRecord: an object (a "form") holding facts about the
   event: logger name, level number, message template, args, time, line number,
   and the error if any. The text is NOT built yet.

2. Levels are just integers. Every level decision is a `>=` comparison:
       NOTSET=0  DEBUG=10  INFO=20  WARNING=30  ERROR=40  CRITICAL=50
   NOTSET means "I haven't chosen, ask my parent."

3. Loggers live in a global registry and form a family tree from the dots in
   their names:  "__main__.ClientLoader" -> "__main__" -> root.
   getLogger("x") always returns the SAME object for the same name.
   getLogger() with no name returns the ROOT, the top of the tree.

4. The journey of logger.info("Inserted %d rows", 3):
     Gate 1: is 20 >= the logger's effective level? (inherited from root if
             NOTSET). If not, stop immediately. Nothing else happens.
     Build the LogRecord.
     Propagation: walk UP the tree, logger -> parent -> ... -> root, handing
             the record to every handler found on the way. Ours are on root.
     Gate 2: each handler checks the record against ITS OWN level.
     Format: the handler's Formatter fills the template using the record's
             fields, like:  "%(name)s ..." % record_fields
     Write:  the handler sends the finished line to its destination.

5. A handler = one destination.
     FileHandler   -> a file on disk (appends, flushes each line)
     StreamHandler -> sys.stderr, the terminal's error channel (channel 2).
                      print() uses stdout (channel 1). The terminal shows both,
                      but they are separate pipes; that's why `2>&1` was needed
                      to grep tracebacks.

6. If NO handler exists anywhere in the tree, Python uses a built-in emergency
   handler ("lastResort") that prints only WARNING and above, unformatted.
   That's why INFO silently vanishes when you forget to call setup_logging().
"""

import logging

# The template every log line follows.
# Each %(field)s is filled from the LogRecord's fields (old-style % formatting
# with a dictionary). Common fields:
#   %(asctime)s    the record's time, made human-readable
#   %(levelname)s  "INFO", "WARNING", ...
#   %(name)s       the logger's name -> which file/class wrote the line
#   %(message)s    your message with the args filled in
#   %(lineno)d     the line number of the log call (optional, not used here)
# Capitals = a constant: defined once, never changed while the program runs.
LOG_FORMAT = "%(asctime)s - %(levelname)s - %(name)s - %(message)s"


def setup_logging(
    log_file: str = "app.log",
    console_level: int = logging.INFO,
    file_level: int = logging.DEBUG,
) -> None:
    """Configure logging once for the whole program.

    Sends every record to two destinations, each with its own level:
      - the file   (default DEBUG and above): full detail, for investigating later
      - the console (default INFO and above): readable progress for a person watching

    Args:
        log_file: path of the log file. Appended to on every run, never overwritten.
        console_level: lowest level shown in the terminal. Pass logging.DEBUG for a
            --verbose mode, e.g.  setup_logging(console_level=logging.DEBUG)
        file_level: lowest level written to the file.

    Why this is a function and not top-level code:
        Importing this file must not change anything (no side effects on import).
        Logging is configured only when an entry point CALLS this function.
    """
    # The root logger: the top of the logger tree.
    # Every logger in every file sends its records up to here (propagation),
    # so attaching handlers HERE means every logger in the program uses them.
    root = logging.getLogger()

    # Guard against double setup.
    # root.handlers is a plain list. Calling this function twice would APPEND
    # two more handlers, and every log line would then be written twice.
    # An empty list is False, so the first call passes through.
    if root.handlers:
        return

    # Gate 1: the logger's own level, checked BEFORE any handler sees the record.
    # Set it to the LOWEST level any handler needs (DEBUG).
    # If this were INFO, DEBUG records would be thrown away here, and the file
    # handler's DEBUG setting below would never receive anything.
    # Rule: open the gate wide at the logger; let each handler decide.
    root.setLevel(logging.DEBUG)

    # Turns a LogRecord into a line of text using LOG_FORMAT.
    # A separate object, so handlers can share one (as here) or each use its own.
    formatter = logging.Formatter(LOG_FORMAT)

    # Destination 1: the log file.
    # Opens the file in append mode and keeps it open; each record becomes one
    # line, flushed to disk so a crash doesn't lose it.
    # To start fresh each run instead, use: logging.FileHandler(log_file, mode="w")
    file_handler = logging.FileHandler(log_file)
    file_handler.setLevel(file_level)        # Gate 2 for the file
    file_handler.setFormatter(formatter)     # without this: bare message only

    # Destination 2: the terminal.
    # StreamHandler() writes to sys.stderr by default (channel 2), the same
    # channel Python uses for tracebacks, so logs don't mix with real output
    # a program prints on stdout.
    console_handler = logging.StreamHandler()
    console_handler.setLevel(console_level)  # Gate 2 for the terminal
    console_handler.setFormatter(formatter)

    # Attach both destinations to the root.
    # From now on, a record that passes Gate 1 reaches both handlers, and each
    # one keeps or skips it based on its own level.
    root.addHandler(file_handler)
    root.addHandler(console_handler)


# ---------------------------------------------------------------------------
# Worked example: what happens to two calls with the defaults above
# ---------------------------------------------------------------------------
#   logger.info("Inserted 3 rows")      level 20
#       Gate 1: 20 >= 10 (root DEBUG)  -> pass
#       File:   20 >= 10               -> written to app.log
#       Console: 20 >= 20              -> shown in terminal
#
#   logger.debug("Clients: [...]")      level 10
#       Gate 1: 10 >= 10               -> pass
#       File:   10 >= 10               -> written to app.log
#       Console: 10 >= 20? NO          -> not shown
#
# That one difference (DEBUG in the file, not on screen) is the proof that
# the two-gate system works.
#
# Why logger.info("... %d", n) instead of an f-string:
#   With %d, the text is only built AFTER the record passes the gates.
#   An f-string builds the text BEFORE the call, even if it's then discarded.
#   One line: no difference. A million DEBUG lines with DEBUG off: big difference.