-- CREATE TABLE transactions (
--    Trans_id	INTEGER PRIMARY KEY,
--    Content_id	INTEGER,
--    User_id	INTEGER,
--    BorrowDate	TEXT NOT NULL,
--    Period		INTEGER,
--    ReturnDate	TEXT,
--    Payment		REAL,
--    FOREIGN KEY(Content_id) REFERENCES content(Content_id),
--    FOREIGN KEY(User_id) REFERENCES user(user_id) );


INSERT INTO transactions VALUES(1, 9, 1, '2020-11-12', 10, NULL, NULL);
INSERT INTO transactions VALUES(2, 9, 4, '2020-11-13', 10, NULL, NULL);
INSERT INTO transactions VALUES(3, 7, 5, '2020-11-05', 10, '2020-11-12', 24.5);

