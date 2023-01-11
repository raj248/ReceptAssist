create table USERS(
    Username varchar(20),
     Password varchar(50),
     Name varchar(50),
     Phone varchar(15),
     Type varchar(10) check(Type in ("ADMIN","OPERATOR","USER")),
     Primary Key(Username));

 insert into USERS value ("root","abc123","Bell","8800862784","ADMIN");

 Create Table COMPLAINER_REGISTRATION(
 Name varchar(50) NOT NULL,
 Email varchar(255),
 Registration_date date,
 Registration_time time,
 Registration_timestamp varchar(20),
 Complainer_id int AUto_increment Primary Key);

 insert into COMPLAINER_REGISTRATION(Name,Email,Registration_date,Registration_time,Registration_timestamp) value ("Zedd","zed007281@gmail.com",curdate(),curtime(),current_timestamp());
 insert into COMPLAINER_REGISTRATION(Name,Email,Registration_date,Registration_time,Registration_timestamp) value ("bear","bearFF281@gmail.com",curdate(),curtime(),current_timestamp());


Create Table COMPLAINT_REGISTER(
     Complaint_title varchar(200),
     Complaint_detail varchar(5000),
     Proof_img_file varchar(500),
     Complainer_id_fk int,
     Is_approved_by_admin varchar(5),
     Complaint_date date,
     Complaint_time time,
     Complaint_timestamp varchar(20),
     Complaint_id int auto_increment Primary Key,
     Foreign key(Complainer_id_fk) references COMPLAINER_REGISTRATION(Complainer_id) on update cascade on delete set null);
-- insert into COMPLAINT_REGISTER(Complaint_title,Complaint_detail,Proof_img_file,Complainer_id_fk,Is_approved_by_admin,Complaint_date,Complaint_time,Complaint_timestamp) value ()
insert into COMPLAINT_REGISTER(Complaint_title,Complaint_detail,Proof_img_file,Complainer_id_fk,Is_approved_by_admin,Complaint_date,Complaint_time,Complaint_timestamp) value ("Server down","Server not responding since 2AM Friday, showing 404 Error","./images/abc.jpg",2,"False",curdate(), curtime(), current_timestamp());

 Create Table COMMENTS(
     Comment_text varchar(2000),
     Complaint_id_fk int,
     Commenter_id varchar(20),
     Date date,
     Time time,
     Timestamp varchar(20),
     Id int auto_increment,
     Primary Key(Id),
     Foreign key(Complaint_id_fk) references COMPLAINT_REGISTER(Complaint_id) on update cascade on delete set null,
     Foreign key(Commenter_id) references USERS(Username) on update cascade on delete set null); 
-- insert into COMMENTS(Comment_text,Complaint_id_fk,Commenter_id,Date,Time,Timestamp) value ()
insert into COMMENTS(Comment_text,Complaint_id_fk,Commenter_id,Date,Time,Timestamp) value ("Server down for longer than usual, missing files or hacked",1,"root",curdate(), curtime(), current_timestamp());


Create Table COMPLAINT_ALLOTMENT(
     User varchar(20),
     Complaint_id_fk int,
     Status varchar(12) check (Status in ("open","closed","resolved","in_process")),
     Constraint unq_Complaint Unique(User,Complaint_id_fk),
     Foreign key(User) references USERS(Username) on update cascade on delete set null,
     Foreign key(Complaint_id_fk) references COMPLAINT_REGISTER(Complaint_id) on update cascade ON DELETE SET NULL);
insert into COMPLAINT_ALLOTMENT value ("root",1,"in_process");