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
