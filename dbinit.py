import os
import sys

import psycopg2 as dbapi2


INIT_STATEMENTS = [
    """
    CREATE TABLE Author( 
                      AuthorID SERIAL PRIMARY KEY , 
                      name VARCHAR(30), 
                      surname VARCHAR(30),
                      birthDate DATE , 
                      numberOfbooks INTEGER,
                      country VARCHAR(20)
                     );
    CREATE TABLE BookRewiev( 
                      BookRewievID SERIAL PRIMARY KEY ,
                      review INTEGER,
                      PostDate DATE,
                      UserRating INTEGER,
                      lostEdit VARCHAR(50),
                      orginalText VARCHAR(100) 
                     );
                     
    CREATE TABLE Publisher( 
                      PublisherID SERIAL PRIMARY KEY , 
                      name VARCHAR(40), 
                      adress VARCHAR(50),
                      numberOfbooks INTEGER , 
                      establishmentDate DATE ,
                      companyName VARCHAR(50)
                     );
                     
    CREATE TABLE Books( 
                      BookID SERIAL PRIMARY KEY , 
                      Title VARCHAR(20),
                      PageNum INTEGER,
                      BookRewiev INTEGER REFERENCES BookRewiev (BookRewievID) , 
                      PublisherID INTEGER REFERENCES Publisher (PublisherID), 
                      AuthorID INTEGER REFERENCES Author (AuthorID) ,
                      cover VARCHAR(1000)
                     );  
                    
                                          
    CREATE TABLE UserContent( 
                      UserContentID SERIAL PRIMARY KEY , 
                      Vote INTEGER, 
                      VoteNum INTEGER,        
                      Comment VARCHAR(200),
                      FavBook INTEGER REFERENCES Books (BookID),
                      FavAuthor INTEGER REFERENCES Author (AuthorID)
                     );
                     
    CREATE TABLE Users( 
                      UserID SERIAL PRIMARY KEY, 
                      name VARCHAR (50)  NOT NULL, 
                      surname VARCHAR (50)  NOT NULL, 
                      gender VARCHAR (6) NULL, 
                      age VARCHAR (3) NULL,
                      content INTEGER REFERENCES UserContent (UserContentID),
                      email VARCHAR (50) UNIQUE NOT NULL,
                      password VARCHAR (20)  NOT NULL,
                      isAdmin INTEGER
                     );
                     
    INSERT INTO Users (name,surname, email,password,isAdmin) 
    VALUES ('admin','admin','admin@gmail.com', 'admin',1);
    INSERT INTO Users (name, surname, gender, age, email, password)
    VALUES ('Barclay', 'Miell', 'Male', 52, 'bmiell3@sfgate.com', 'jp7PDwLdq');
    INSERT INTO Users (name, surname, gender, age, email, password)
    VALUES ('Stephenie', 'Mackie', 'Female', 39, 'smackie4@ebay.co.uk', 'oHjvgA');
    INSERT INTO Users (name, surname, gender, age, email, password)
    VALUES ('Hewett', 'Grushin', 'Male', 24, 'hgrushin5@state.gov', '05JJUHZzbm');
    INSERT INTO Users (name, surname, gender, age, email, password)
    VALUES ('L;urette', 'O''Cassidy', 'Female', 51, 'locassidy6@4shared.com', 'JNskYpdg');
    INSERT INTO Users (name, surname, gender, age, email, password)
    VALUES ('Vidovic', 'Avesque', 'Male', 34, 'vavesque7@amazon.com', '3Em8lAq60');
    INSERT INTO Users (name, surname, gender, age, email, password)
    VALUES ('Lionello', 'Tippell', 'Male', 39, 'ltippell8@cornell.edu', 'ki3NZPZ');
    INSERT INTO Users (name, surname, gender, age, email, password)
    VALUES ('Sergei', 'Gillani', 'Male', 17, 'sgillani9@buzzfeed.com', '1XXYRPp');
    INSERT INTO Users (name, surname, gender, age, email, password)
    VALUES ('Frasier', 'Weeden', 'Male', 42, 'fweedena@hexun.com', '7VTulLCSQEF9');
    INSERT INTO Users (name, surname, gender, age, email, password)
    VALUES ('Bartolomeo', 'Maddams', 'Male', 56, 'bmaddamsb@moonfruit.com', 'YFcsiuI4');
    INSERT INTO Users (name, surname, gender, age, email, password)     
    VALUES ('Liana', 'Whitlow', 'Female', 38, 'lwhitlowc@wisc.edu', 'erj4fyg');
    INSERT INTO Users (name, surname, gender, age, email, password)
    VALUES ('Patricia', 'Buie', 'Female', 44, 'pbuied@domainmarket.com', 'GaIas7');
    INSERT INTO Users (name, surname, gender, age, email, password)
    VALUES ('Chastity', 'Stripp', 'Female', 29, 'cstrippe@so-net.ne.jp', 'xgnVLdg');
    INSERT INTO Users (name, surname, gender, age, email, password)
    VALUES ('Jandy', 'Haldin', 'Female', 39, 'jhaldinf@de.vu', 'JmugRzVE3');
    INSERT INTO Users (name, surname, gender, age, email, password)
    VALUES ('Dolf', 'Stollwerck', 'Male', 33, 'dstollwerckg@i2i.jp', 'Rbwlr4Sr');
    INSERT INTO Users (name, surname, gender, age, email, password)
    VALUES ('Birk', 'Ormiston', 'Male', 35, 'bormistonh@networksolutions.com', 'SOFfvd1MwWk');
    INSERT INTO Users (name, surname, gender, age, email, password)
    VALUES ('Verna', 'Jacqueminet', 'Female', 44, 'vjacquemineti@histats.com', 'O2HG4ud46rj');
    INSERT INTO Users (name, surname, gender, age, email, password) 
    VALUES ('Jayme', 'Wathey', 'Female', 33, 'jwatheyj@i2i.jp', 'JKmAkO');
    INSERT INTO Users (name, surname, gender, age, email, password)
    VALUES ('Mikaela', 'Lambell', 'Female', 52, 'mlambellk@google.com.hk', 'N9JYvz');
    INSERT INTO Users (name, surname, gender, age, email, password)
    VALUES ('Barr', 'O''Howbane', 'Male', 34, 'bohowbanel@posterous.com', 'Tm5WdNLJv');
    INSERT INTO Users (name, surname, gender, age, email, password)
    VALUES ('Griff', 'Forster', 'Male', 53, 'gforsterm@jiathis.com', 'cnwcNj9H2A');
    INSERT INTO Users (name, surname, gender, age, email, password)
    VALUES ('Vikki', 'Orable', 'Female', 49, 'vorablen@google.nl', '4tvDEZZI');
    INSERT INTO Users (name, surname, gender, age, email, password)
    VALUES ('Laverne', 'Sanja', 'Female', 21, 'lsanjao@cocolog-nifty.com', 'N88VIM387');
    INSERT INTO Publisher(name,adress, numberOfbooks) 
    VALUES ('tonguc','eyub mah.',150);
    INSERT INTO Author(name,surname, numberOfbooks,country) 
    VALUES ('adam','fawer',10,'USA');
    INSERT INTO Books(Title,PageNum, PublisherID,AuthorID ) 
    VALUES ('olasılıksız',250,1,1);
    INSERT INTO Publisher(name,adress, numberOfbooks) 
    VALUES ('alfa','kadıköy',100);
    INSERT INTO Author(name,surname, numberOfbooks,country) 
    VALUES ('ahmet','yıldız',5,'Turkey');
    INSERT INTO Books(Title,PageNum, PublisherID,AuthorID ) 
    VALUES ('oz',350,2,2);
    INSERT INTO Books(Title,PageNum, PublisherID,AuthorID) 
    VALUES ('Guclu hafıza',325,2,2);
    INSERT INTO Publisher (name, adress, numberOfbooks, establishmentDate, companyName) VALUES ('Asoka', '96064 Norway Maple Hill', 31, '1/21/1977', 'Cassin LLC');
INSERT INTO Publisher (name, adress, numberOfbooks, establishmentDate, companyName) VALUES ('Overhold', '03 Oneill Alley', 70, '10/10/1961', 'Ankunding, Macejkovic and Hansen');
INSERT INTO Publisher (name, adress, numberOfbooks, establishmentDate, companyName) VALUES ('Veribet', '99353 Bashford Drive', 27, '8/2/1967', 'Boyle, McCullough and Macejkovic');
INSERT INTO Publisher (name, adress, numberOfbooks, establishmentDate, companyName) VALUES ('Transcof', '7654 Fisk Pass', 42, '9/17/1979', 'Mann Group');
INSERT INTO Publisher (name, adress, numberOfbooks, establishmentDate, companyName) VALUES ('Domainer', '8 Tony Court', 48, '1/5/2002', 'Kris Group');
INSERT INTO Publisher (name, adress, numberOfbooks, establishmentDate, companyName) VALUES ('Zamit', '20 Becker Plaza', 22, '10/24/1970', 'Jerde Group');
INSERT INTO Publisher (name, adress, numberOfbooks, establishmentDate, companyName) VALUES ('Pannier', '3152 Dayton Alley', 72, '11/1/2005', 'Hettinger, Price and Schuster');
INSERT INTO Publisher (name, adress, numberOfbooks, establishmentDate, companyName) VALUES ('Ventosanzap', '589 Fallview Lane', 83, '11/11/2005', 'Jones, Gorczany and Zemlak');
INSERT INTO Publisher (name, adress, numberOfbooks, establishmentDate, companyName) VALUES ('Latlux', '064 Pine View Crossing', 26, '11/23/1996', 'Feeney, Jast and Zboncak');
INSERT INTO Publisher (name, adress, numberOfbooks, establishmentDate, companyName) VALUES ('Bigtax', '41 Sachs Way', 79, '7/13/1976', 'Renner-Osinski');
INSERT INTO Publisher (name, adress, numberOfbooks, establishmentDate, companyName) VALUES ('Namfix', '034 Dorton Center', 27, '11/22/1992', 'McKenzie-Donnelly');
INSERT INTO Publisher (name, adress, numberOfbooks, establishmentDate, companyName) VALUES ('Duobam', '6697 Armistice Parkway', 78, '6/9/2008', 'Hessel, Hirthe and Schinner');
INSERT INTO Publisher (name, adress, numberOfbooks, establishmentDate, companyName) VALUES ('Alpha', '212 Nevada Junction', 49, '3/10/1971', 'Mraz LLC');
INSERT INTO Publisher (name, adress, numberOfbooks, establishmentDate, companyName) VALUES ('Daltfresh', '0429 Doe Crossing Crossing', 11, '1/2/2001', 'Pacocha Group');
INSERT INTO Publisher (name, adress, numberOfbooks, establishmentDate, companyName) VALUES ('Subin', '6037 Bellgrove Plaza', 86, '6/22/1975', 'Larkin, Hudson and Fahey');
INSERT INTO Publisher (name, adress, numberOfbooks, establishmentDate, companyName) VALUES ('Holdlamis', '26333 Holy Cross Drive', 50, '7/9/1984', 'Skiles LLC');
INSERT INTO Publisher (name, adress, numberOfbooks, establishmentDate, companyName) VALUES ('Subin', '79 South Circle', 51, '2/14/2013', 'Zieme-Kulas');
INSERT INTO Publisher (name, adress, numberOfbooks, establishmentDate, companyName) VALUES ('Zontrax', '02556 Dunning Street', 17, '7/19/2012', 'Kessler, Grant and Lueilwitz');
INSERT INTO Publisher (name, adress, numberOfbooks, establishmentDate, companyName) VALUES ('Y-Solowarm', '187 Farragut Park', 28, '1/22/2007', 'Gleason LLC');
INSERT INTO Publisher (name, adress, numberOfbooks, establishmentDate, companyName) VALUES ('Bamity', '26493 Bunker Hill Drive', 5, '12/7/1964', 'Abshire, Jones and Ledner');
INSERT INTO Publisher (name, adress, numberOfbooks, establishmentDate, companyName) VALUES ('Sub-Ex', '6884 Stoughton Lane', 72, '5/27/1990', 'Smitham-Connelly');
INSERT INTO Publisher (name, adress, numberOfbooks, establishmentDate, companyName) VALUES ('Ventosanzap', '91704 Springview Place', 76, '8/18/2005', 'Blanda-Carter');
INSERT INTO Publisher (name, adress, numberOfbooks, establishmentDate, companyName) VALUES ('Regrant', '7285 Granby Center', 89, '11/15/1973', 'Wilkinson Group');
INSERT INTO Publisher (name, adress, numberOfbooks, establishmentDate, companyName) VALUES ('Ronstring', '3 Mcguire Center', 19, '11/6/1966', 'Cummings, Haley and Carter');
INSERT INTO Publisher (name, adress, numberOfbooks, establishmentDate, companyName) VALUES ('Bigtax', '7 4th Court', 52, '2/5/2000', 'Denesik-Schneider');

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
