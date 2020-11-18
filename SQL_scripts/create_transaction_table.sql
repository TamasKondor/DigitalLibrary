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
