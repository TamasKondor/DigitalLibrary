PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;
CREATE TABLE content (
    Content_id	INTEGER PRIMARY KEY,
    Type_id     INTEGER,	
    Name	TEXT NOT NULL,
    Author      TEXT NOT NULL,
    Stock	INTEGER,
    Available   INTEGER,
    Price	REAL,
    Active	INTEGER,
    FOREIGN KEY(Type_id) REFERENCES type(Type_id)
);
INSERT INTO content VALUES(1,1,'Oracle Database 10g','Kevin Loney',10,10,1.9499999999999999555,1);
INSERT INTO content VALUES(2,1,'Oracle Exercise Book','Marlene Theriault',10,10,1.75,1);
INSERT INTO content VALUES(3,1,'MacOS X Leopard Handbook','Gabor Ferenczy',10,10,2.4500000000000001776,1);
INSERT INTO content VALUES(4,1,'Computer Architectures','Dezso Sima',5,5,3.1299999999999998934,1);
INSERT INTO content VALUES(5,2,'Free Picture Library','Arthur Pentington',3,3,1.5,1);
INSERT INTO content VALUES(6,2,'Background Templates','FSF org.',20,20,0.0,1);
INSERT INTO content VALUES(7,3,'The Real Hackers','Eric S. Raymond ',5,5,2.2999999999999998223,1);
INSERT INTO content VALUES(8,3,'Business at the Speed of Thought','Bill Gates ',3,3,3.5,1);
INSERT INTO content VALUES(9,4,'Python for Beginners','Mosh Hamedani',4,2,4.0999999999999996447,1);
INSERT INTO content VALUES(10,4,'Learn Python in 12 Hours','Edureka!',7,7,3.75,1);
INSERT INTO content VALUES(11,5,'Byte Magazine - Vol 1 (1975)','Green Publishing Inc.',1,1,1.75,1);
INSERT INTO content VALUES(12,5,'Byte Magazine - Vol 2 (1976)','Green Publishing Inc.',1,1,1.75,1);
INSERT INTO content VALUES(13,5,'Byte Magazine - Vol 3 (1977)','Green Publishing Inc.',1,1,1.75,1);
CREATE TABLE transactions (
    Trans_id	INTEGER PRIMARY KEY,
    Content_id	INTEGER,
    User_id	INTEGER,
    BorrowDate	TEXT NOT NULL,
    Period	INTEGER,
    ReturnDate	TEXT,
    Payment	REAL,
    FOREIGN KEY(Content_id) REFERENCES content(Content_id),
    FOREIGN KEY(User_id) REFERENCES user(user_id)
);
INSERT INTO transactions VALUES(1,9,1,'2020-11-12',10,NULL,NULL);
INSERT INTO transactions VALUES(2,9,4,'2020-11-13',10,NULL,NULL);
INSERT INTO transactions VALUES(3,7,5,'2020-11-05',10,'2020-11-12',24.5);
CREATE TABLE type (
    Type_id	INTEGER PRIMARY KEY,
    TypeName 	TEXT
);
INSERT INTO type VALUES(1,'eBook');
INSERT INTO type VALUES(2,'Image');
INSERT INTO type VALUES(3,'Audio');
INSERT INTO type VALUES(4,'Video');
INSERT INTO type VALUES(5,'Digital documents');
INSERT INTO type VALUES(6,'Digital media');
CREATE TABLE user (
    User_id	INTEGER PRIMARY KEY,
    FName	TEXT NOT NULL,
    LName	TEXT NOT NULL,
    Added	TEXT NOT NULL,
    Role	TEXT NOT NULL
);
INSERT INTO user VALUES(1,'John','Doe','2020-11-10','User');
INSERT INTO user VALUES(2,'Tibor','Acs','2020-11-11','Librarian');
INSERT INTO user VALUES(3,'Elek','Test','2020-11-12','Librarian');
INSERT INTO user VALUES(4,'Jane','Doe','2020-11-13','User');
INSERT INTO user VALUES(5,'Rob','Schafer','2020-11-14','User');
COMMIT;
