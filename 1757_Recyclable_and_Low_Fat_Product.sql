create Table Products{
    product_id int,
    low_fats ENUM('Y', 'N'),
    recyclable  ENUM('Y','N')
};

select product_id from product_id where low_fats='Y' and recyclable='Y'