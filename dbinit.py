import os
import sys

import psycopg2 as dbapi2


INIT_STATEMENTS = [
    """
    CREATE TABLE Users( 
                      UserID SERIAL PRIMARY KEY, 
                      name VARCHAR (50) UNIQUE NOT NULL, 
                      surname VARCHAR (50) UNIQUE NOT NULL, 
                      gender VARCHAR (6) NULL, 
                      age VARCHAR (3) NULL,
                      content INTEGER REFERENCES UserContent (UserContentID),
                      email VARCHAR (50) UNIQUE NOT NULL,
                      password VARCHAR (20) UNIQUE NOT NULL,
                      isAdmin INTEGER
                     );
                     
    CREATE TABLE UserContent( 
                      UserContentID SERIAL PRIMARY KEY , 
                      Vote INTEGER, 
                      VoteNum INTEGER,        
                      Comment VARCHAR(200),
                      FavBook INTEGER REFERENCES Books (BookID),
                      FavAuthor INTEGER REFERENCES Author (AuthorID)
                     );
                     
    CREATE TABLE Publisher( 
                      PublisherID SERIAL PRIMARY KEY , 
                      name VARCHAR(40), 
                      adress VARCHAR(50),
                      numberOfbooks INTEGER , 
                      establishmentDate TIME ,
                      logo VARBINARY(8000)
                     );
    CREATE TABLE Author( 
                      AuthorID SERIAL PRIMARY KEY , 
                      name VARCHAR(30), 
                      surname VARCHAR(30),
                      birthDate TIME , 
                      numberOfbooks INTEGER,
                      country VARCHAR(20)
                     );
                     
    CREATE TABLE Books( 
                      BookID SERIAL PRIMARY KEY , 
                      Title VARCHAR(20),
                      PageNum INTEGER,
                      BookRewiev INTEGER REFERENCES BookRewiev (BookRewievID) , 
                      PublisherID INTEGER REFERENCES Publisher (PublisherID), 
                      AuthorID INTEGER REFERENCES Author (AuthorID)               
                     );   
 
    CREATE TABLE BookRewiev( 
                      BookRewievID SERIAL PRIMARY KEY , 
                      UserID INTEGER REFERENCES Users (UserID), 
                      BookID INTEGER REFERENCES Books  (BookID), 
                      review INTEGER,
                      PostDate TIME,
                      UserRating INTEGER,
                      lostEdit VARCHAR(50),
                      orginalText VARCHAR(100) 
                     ); 
    INSERT INTO Users (name,surname, email,password,isAdmin) 
    VALUES ('admin','admin','admin@gmail.com', 'admin',1);
    """
]


def initialize(url):
    with dbapi2.connect(url) as connection:
        cursor = connection.cursor()
        for statement in INIT_STATEMENTS:
            cursor.execute(statement)
        cursor.close()


if __name__ == "__main__":
    url = os.getenv("DATABASE_URL")
    if url is None:
        print("Usage: DATABASE_URL=url python dbinit.py", file=sys.stderr)
        sys.exit(1)
    initialize(url)
