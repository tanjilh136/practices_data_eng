class balance_management:
    def __init__(self,val=0.0):
        self._val = val
    def display_balance(self):
        print("the Balance {}".format(self._val))
    def add_money(self, value):
        self._val = self._val + value
    def purchase_action(self,value):
        if value > self._val:
            print("Inadequate funds")
        else:
            self._val=self._val-value

    @property
    def val(self):
        return self._val

    @val.setter
    def val(self,value):
        if value<=0:
            print("Negative can't be there")
        else:
            self._val= value

class Manager:
    def __init__(self, name= None, contact= None, brnach = None):
        self.name = name
        self.contact = contact
        self.branch = brnach

    def manager_details_disp(self):
        print(f" MANAGER name: {self.name}")
        print("contact{}\t email {}\t".format(self.Contact,self.email))

    def set_manager(self, name, contact, branch):
        self.name = name
        self.contact = contact
        self.branch = branch               

class Clients(balance_management, Manager):
    def __init__(self, f_name, l_name, Contact, email, val=0.0, name=None, contact=None, branch=None):
        balance_management.__init__(self,val)
        Manager.__init__(self,name,contact,branch)
        self.f_name = f_name
        self.l_name = l_name
        self.Contact = Contact
        self.email = email

    def display(self):
        print(f" HI {self.f_name+" "+ self.l_name} here is your Account details")
        print("contact{}\t email {}\t".format(self.Contact,self.email))
    def setname(self,f_name, l_name):
        self.f_name = f_name
        self.l_name = l_name

client1 = Clients("Tanjil", "Hasan", "+351939962733", "tanjilhasan689@gmail.com")
client1.display()
client1.set_manager("Paulo","Paulo@gmail.com", "Khagan")
client1.add_money(9000)
client1.purchase_action(200)
client1.purchase_action(100)
client1.display_balance()
print(client1.val)