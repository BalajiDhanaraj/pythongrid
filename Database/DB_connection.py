import mysql.connector

mydb = mysql.connector.connect(

    host="localhost",
    user="root",
    password="root@2363",
    database='pydb'

)


mycursor = mydb.cursor()

mycursor.execute()


create table selenium(
tutorial_id INT NOT NULL auto_increment,
tutorial_title varchar(100) NOT NULL,
tutorial_author varchar(40) NOT NULL,
submission_date date,
primary key (tutorial_id)
);



insert into selenium values(2,"dev","cory",now());

















