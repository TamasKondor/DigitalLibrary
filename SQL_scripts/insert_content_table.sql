-- CREATE TABLE content (
--    Content_id	INTEGER PRIMARY KEY,
--    Type_id     INTEGER,	
--    Name	TEXT NOT NULL,
--    Author      TEXT NOT NULL,
--    Stock	INTEGER,
--    Available   INTEGER,
--    Price	REAL,
--    Active	INTEGER 
--    FOREIGN KEY(Type_id) REFERENCES type(type_id)
-- );

INSERT INTO content VALUES(1, 1, 'Oracle Database 10g', 'Kevin Loney', 10, 10, 1.95, 1);
INSERT INTO content VALUES(2, 1, 'Oracle Exercise Book', 'Marlene Theriault', 10, 10, 1.75, 1);
INSERT INTO content VALUES(3, 1, 'MacOS X Leopard Handbook', 'Gabor Ferenczy', 10, 10, 2.45, 1);
INSERT INTO content VALUES(4, 1, 'Computer Architectures', 'Dezso Sima', 5, 5, 3.13, 1);
INSERT INTO content VALUES(5, 2, 'Free Picture Library', 'Arthur Pentington', 3, 3, 1.50, 1);
INSERT INTO content VALUES(6, 2, 'Background Templates', 'FSF org.', 20, 20, 00.00, 1);
INSERT INTO content VALUES(7, 3, 'The Real Hackers', 'Eric S. Raymond ', 5, 5, 2.30, 1);
INSERT INTO content VALUES(8, 3, 'Business at the Speed of Thought', 'Bill Gates ', 3, 3, 3.50, 1);
INSERT INTO content VALUES(9, 4, 'Python for Beginners', 'Mosh Hamedani', 4, 2, 4.10, 1);
INSERT INTO content VALUES(10, 4, 'Learn Python in 12 Hours', 'Edureka!', 7, 7, 3.75, 1);
INSERT INTO content VALUES(11, 5, 'Byte Magazine - Vol 1 (1975)', 'Green Publishing Inc.', 1, 1, 1.75, 1);
INSERT INTO content VALUES(12, 5, 'Byte Magazine - Vol 2 (1976)', 'Green Publishing Inc.', 1, 1, 1.75, 1);
INSERT INTO content VALUES(13, 5, 'Byte Magazine - Vol 3 (1977)', 'Green Publishing Inc.', 1, 1, 1.75, 1);


