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
                      country VARCHAR(40)
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
INSERT INTO Author (name, surname, birthDate, numberOfbooks, country) VALUES ('Collin', 'Clyant', '6/30/1916', 18, 'South Korea');
INSERT INTO Author (name, surname, birthDate, numberOfbooks, country) VALUES ('Clementina', 'Boatwright', '5/22/1931', 24, 'Portugal');
INSERT INTO Author (name, surname, birthDate, numberOfbooks, country) VALUES ('Alano', 'Colqueran', '1/3/1924', 23, 'Russia');
INSERT INTO Author (name, surname, birthDate, numberOfbooks, country) VALUES ('Vin', 'Adamini', '9/27/1946', 16, 'Somalia');
INSERT INTO Author (name, surname, birthDate, numberOfbooks, country) VALUES ('Menard', 'Jorcke', '10/16/1950', 20, 'Sweden');
INSERT INTO Author (name, surname, birthDate, numberOfbooks, country) VALUES ('Ilka', 'Kinvan', '7/17/1952', 17, 'Greece');
INSERT INTO Author (name, surname, birthDate, numberOfbooks, country) VALUES ('Dirk', 'Blakiston', '8/10/1936', 6, 'Lithuania');
INSERT INTO Author (name, surname, birthDate, numberOfbooks, country) VALUES ('Starla', 'Berney', '1/29/1981', 12, 'Greece');
INSERT INTO Author (name, surname, birthDate, numberOfbooks, country) VALUES ('Emili', 'Creddon', '8/26/1960', 12, 'China');
INSERT INTO Author (name, surname, birthDate, numberOfbooks, country) VALUES ('Alaine', 'Laurentin', '1/5/1954', 19, 'Mexico');
INSERT INTO Author (name, surname, birthDate, numberOfbooks, country) VALUES ('Sonny', 'Favelle', '6/18/1981', 6, 'Peru');
INSERT INTO Author (name, surname, birthDate, numberOfbooks, country) VALUES ('Jennilee', 'De Michetti', '9/20/1926', 18, 'Tajikistan');
INSERT INTO Author (name, surname, birthDate, numberOfbooks, country) VALUES ('Hertha', 'Stallon', '3/18/1925', 16, 'Poland');
INSERT INTO Author (name, surname, birthDate, numberOfbooks, country) VALUES ('Magdalene', 'Shannon', '5/31/1961', 7, 'Philippines');
INSERT INTO Author (name, surname, birthDate, numberOfbooks, country) VALUES ('Marylin', 'Larrat', '6/14/1917', 1, 'Azerbaijan');
INSERT INTO Author (name, surname, birthDate, numberOfbooks, country) VALUES ('Fred', 'Towe', '3/21/1955', 16, 'Russia');
INSERT INTO Author (name, surname, birthDate, numberOfbooks, country) VALUES ('Derrek', 'Berks', '11/14/1922', 13, 'Montserrat');
INSERT INTO Author (name, surname, birthDate, numberOfbooks, country) VALUES ('Sashenka', 'Agnew', '8/11/1949', 19, 'Indonesia');
INSERT INTO Author (name, surname, birthDate, numberOfbooks, country) VALUES ('Morena', 'Arthey', '12/31/1974', 24, 'China');
INSERT INTO Author (name, surname, birthDate, numberOfbooks, country) VALUES ('Faith', 'Cazereau', '5/3/1916', 16, 'Iran');
INSERT INTO Author (name, surname, birthDate, numberOfbooks, country) VALUES ('Stearne', 'Peris', '3/3/1940', 14, 'Indonesia');
INSERT INTO Author (name, surname, birthDate, numberOfbooks, country) VALUES ('Alisha', 'Jotcham', '5/12/1917', 18, 'Indonesia');
INSERT INTO Author (name, surname, birthDate, numberOfbooks, country) VALUES ('Dulcea', 'Busfield', '3/9/1918', 9, 'Indonesia');
INSERT INTO Author (name, surname, birthDate, numberOfbooks, country) VALUES ('Coreen', 'Sidebotham', '5/7/1978', 21, 'China');
INSERT INTO Author (name, surname, birthDate, numberOfbooks, country) VALUES ('Kally', 'Lyttle', '7/23/1928', 4, 'Kazakhstan');
INSERT INTO Author (name, surname, birthDate, numberOfbooks, country) VALUES ('Flss', 'MacAnespie', '12/31/1911', 15, 'Georgia');
INSERT INTO Author (name, surname, birthDate, numberOfbooks, country) VALUES ('Paulie', 'Venus', '4/15/1958', 4, 'Russia');
INSERT INTO Author (name, surname, birthDate, numberOfbooks, country) VALUES ('Wit', 'Care', '5/26/1912', 25, 'Philippines');
INSERT INTO Author (name, surname, birthDate, numberOfbooks, country) VALUES ('Anni', 'Torre', '10/14/1936', 12, 'North Korea');
INSERT INTO Author (name, surname, birthDate, numberOfbooks, country) VALUES ('Walden', 'Westnedge', '5/31/1939', 3, 'Nigeria');
INSERT INTO Author (name, surname, birthDate, numberOfbooks, country) VALUES ('Kris', 'Legrand', '6/2/1911', 4, 'Dominican Republic');
INSERT INTO Author (name, surname, birthDate, numberOfbooks, country) VALUES ('Pail', 'Daveridge', '7/30/1952', 10, 'Japan');
INSERT INTO Author (name, surname, birthDate, numberOfbooks, country) VALUES ('Nicolai', 'Segges', '11/22/1967', 15, 'Greece');
INSERT INTO Author (name, surname, birthDate, numberOfbooks, country) VALUES ('Ron', 'Beckhouse', '4/8/1924', 18, 'Macedonia');
INSERT INTO Author (name, surname, birthDate, numberOfbooks, country) VALUES ('Loutitia', 'Sturt', '5/12/1927', 3, 'China');
INSERT INTO Author (name, surname, birthDate, numberOfbooks, country) VALUES ('Mark', 'Huggard', '8/19/1930', 7, 'China');
INSERT INTO Author (name, surname, birthDate, numberOfbooks, country) VALUES ('Andris', 'Vigours', '1/18/1978', 9, 'Indonesia');
INSERT INTO Author (name, surname, birthDate, numberOfbooks, country) VALUES ('Nani', 'Plows', '2/7/1978', 6, 'Central African Republic');
INSERT INTO Author (name, surname, birthDate, numberOfbooks, country) VALUES ('Jock', 'Kepe', '12/22/1918', 20, 'Slovenia');
INSERT INTO Author (name, surname, birthDate, numberOfbooks, country) VALUES ('Rodolphe', 'Blachford', '11/28/1952', 9, 'Portugal');
INSERT INTO Author (name, surname, birthDate, numberOfbooks, country) VALUES ('Jamima', 'Rottenbury', '2/18/1922', 25, 'Sweden');
INSERT INTO Author (name, surname, birthDate, numberOfbooks, country) VALUES ('Allianora', 'Crawshaw', '9/14/1975', 22, 'Greece');
INSERT INTO Author (name, surname, birthDate, numberOfbooks, country) VALUES ('Clarice', 'Sondland', '5/8/1978', 1, 'Indonesia');
INSERT INTO Author (name, surname, birthDate, numberOfbooks, country) VALUES ('Heywood', 'Skyrm', '4/28/1976', 5, 'Peru');
INSERT INTO Author (name, surname, birthDate, numberOfbooks, country) VALUES ('Devin', 'Clackson', '11/14/1955', 12, 'China');
INSERT INTO Author (name, surname, birthDate, numberOfbooks, country) VALUES ('Finlay', 'Menier', '12/1/1957', 22, 'Russia');
INSERT INTO Author (name, surname, birthDate, numberOfbooks, country) VALUES ('Harri', 'Dieton', '3/14/1967', 10, 'China');
INSERT INTO Author (name, surname, birthDate, numberOfbooks, country) VALUES ('Melessa', 'Colebourn', '1/24/1967', 23, 'Thailand');
INSERT INTO Author (name, surname, birthDate, numberOfbooks, country) VALUES ('Stephan', 'Campion', '10/15/1926', 14, 'China');
INSERT INTO Author (name, surname, birthDate, numberOfbooks, country) VALUES ('Saloma', 'Norcott', '8/22/1952', 17, 'China');
INSERT INTO Author (name, surname, birthDate, numberOfbooks, country) VALUES ('Olive', 'Meiner', '4/16/1915', 19, 'Philippines');
INSERT INTO Author (name, surname, birthDate, numberOfbooks, country) VALUES ('Killy', 'Tallboy', '3/24/1917', 5, 'Portugal');
INSERT INTO Author (name, surname, birthDate, numberOfbooks, country) VALUES ('Loretta', 'Andrin', '2/13/1924', 6, 'Argentina');
INSERT INTO Author (name, surname, birthDate, numberOfbooks, country) VALUES ('Gifford', 'Angel', '6/1/1922', 19, 'Belarus');
INSERT INTO Author (name, surname, birthDate, numberOfbooks, country) VALUES ('Brynna', 'Dell Casa', '5/20/1954', 23, 'Brazil');
INSERT INTO Author (name, surname, birthDate, numberOfbooks, country) VALUES ('Imogen', 'Sergeaunt', '8/1/1961', 23, 'Costa Rica');
INSERT INTO Author (name, surname, birthDate, numberOfbooks, country) VALUES ('Guenna', 'Baptiste', '6/1/1969', 17, 'Cameroon');
INSERT INTO Author (name, surname, birthDate, numberOfbooks, country) VALUES ('Nathanial', 'Penquet', '12/13/1961', 22, 'Peru');
INSERT INTO Author (name, surname, birthDate, numberOfbooks, country) VALUES ('Debra', 'Bendson', '4/3/1914', 2, 'Indonesia');
INSERT INTO Author (name, surname, birthDate, numberOfbooks, country) VALUES ('Kassey', 'Walthew', '9/17/1982', 21, 'Armenia');
INSERT INTO Author (name, surname, birthDate, numberOfbooks, country) VALUES ('Jere', 'Whorton', '6/5/1961', 19, 'Kiribati');
INSERT INTO Author (name, surname, birthDate, numberOfbooks, country) VALUES ('Warden', 'Brunotti', '3/2/1957', 18, 'Indonesia');
INSERT INTO Author (name, surname, birthDate, numberOfbooks, country) VALUES ('Eduard', 'Stitcher', '7/12/1951', 3, 'Bahamas');
INSERT INTO Author (name, surname, birthDate, numberOfbooks, country) VALUES ('Kara', 'Giovannelli', '11/20/1951', 25, 'Indonesia');
INSERT INTO Author (name, surname, birthDate, numberOfbooks, country) VALUES ('Rosalinde', 'Lintall', '1/26/1959', 22, 'China');
INSERT INTO Author (name, surname, birthDate, numberOfbooks, country) VALUES ('Lise', 'Lardge', '12/18/1938', 20, 'France');
INSERT INTO Author (name, surname, birthDate, numberOfbooks, country) VALUES ('Mureil', 'Bythway', '12/31/1933', 12, 'Japan');
INSERT INTO Author (name, surname, birthDate, numberOfbooks, country) VALUES ('Maurise', 'Leak', '8/21/1931', 13, 'South Africa');
INSERT INTO Author (name, surname, birthDate, numberOfbooks, country) VALUES ('Guendolen', 'Bremmell', '9/10/1913', 4, 'China');
INSERT INTO Author (name, surname, birthDate, numberOfbooks, country) VALUES ('Oren', 'Sebrook', '2/28/1928', 16, 'Croatia');
INSERT INTO Author (name, surname, birthDate, numberOfbooks, country) VALUES ('Terrye', 'Conwell', '8/26/1973', 20, 'Sweden');
INSERT INTO Author (name, surname, birthDate, numberOfbooks, country) VALUES ('Rob', 'Wreford', '1/9/1930', 6, 'Philippines');
INSERT INTO Author (name, surname, birthDate, numberOfbooks, country) VALUES ('Elle', 'Botterill', '10/7/1923', 2, 'Indonesia');
INSERT INTO Author (name, surname, birthDate, numberOfbooks, country) VALUES ('Becky', 'Stalley', '6/9/1941', 3, 'Mexico');
INSERT INTO Author (name, surname, birthDate, numberOfbooks, country) VALUES ('Ardeen', 'Landrean', '7/29/1953', 20, 'Nigeria');
INSERT INTO Author (name, surname, birthDate, numberOfbooks, country) VALUES ('Meghan', 'Denley', '3/10/1974', 8, 'China');
INSERT INTO Author (name, surname, birthDate, numberOfbooks, country) VALUES ('Alleyn', 'Lazarus', '5/9/1943', 21, 'Palestinian Territory');
INSERT INTO Author (name, surname, birthDate, numberOfbooks, country) VALUES ('Mylo', 'Ashburner', '11/15/1918', 20, 'China');
INSERT INTO Author (name, surname, birthDate, numberOfbooks, country) VALUES ('Kristofor', 'Olphert', '9/14/1945', 2, 'China');
INSERT INTO Author (name, surname, birthDate, numberOfbooks, country) VALUES ('Dario', 'Guard', '5/17/1924', 14, 'Brazil');
INSERT INTO Author (name, surname, birthDate, numberOfbooks, country) VALUES ('Phaedra', 'Saw', '3/12/1955', 6, 'Luxembourg');
INSERT INTO Author (name, surname, birthDate, numberOfbooks, country) VALUES ('Maryann', 'Golsby', '10/25/1913', 4, 'Poland');
INSERT INTO Author (name, surname, birthDate, numberOfbooks, country) VALUES ('Linnie', 'Lincke', '2/6/1942', 12, 'China');
INSERT INTO Author (name, surname, birthDate, numberOfbooks, country) VALUES ('Gearalt', 'Bangiard', '11/24/1929', 23, 'Indonesia');
INSERT INTO Author (name, surname, birthDate, numberOfbooks, country) VALUES ('Bron', 'Froment', '8/23/1918', 1, 'Japan');
INSERT INTO Author (name, surname, birthDate, numberOfbooks, country) VALUES ('Burr', 'Woodroff', '8/9/1957', 10, 'Togo');
INSERT INTO Author (name, surname, birthDate, numberOfbooks, country) VALUES ('Britteny', 'Suett', '4/29/1948', 21, 'Thailand');
INSERT INTO Author (name, surname, birthDate, numberOfbooks, country) VALUES ('Pavel', 'Vickar', '1/2/1923', 14, 'Malaysia');
INSERT INTO Author (name, surname, birthDate, numberOfbooks, country) VALUES ('Elfrieda', 'Goligly', '10/28/1946', 25, 'Afghanistan');
INSERT INTO Author (name, surname, birthDate, numberOfbooks, country) VALUES ('Launce', 'Lodemann', '3/27/1957', 18, 'Suriname');
INSERT INTO Author (name, surname, birthDate, numberOfbooks, country) VALUES ('Clayborn', 'Souley', '10/15/1934', 19, 'China');
INSERT INTO Author (name, surname, birthDate, numberOfbooks, country) VALUES ('Petra', 'Simonian', '2/7/1959', 7, 'Norway');
INSERT INTO Author (name, surname, birthDate, numberOfbooks, country) VALUES ('Donetta', 'Webbe', '12/19/1915', 3, 'China');
INSERT INTO Author (name, surname, birthDate, numberOfbooks, country) VALUES ('Evanne', 'Stratford', '12/10/1931', 8, 'Indonesia');
INSERT INTO Author (name, surname, birthDate, numberOfbooks, country) VALUES ('Moll', 'Palley', '11/25/1939', 18, 'Colombia');
INSERT INTO Author (name, surname, birthDate, numberOfbooks, country) VALUES ('Ramon', 'Arzu', '1/16/1932', 21, 'Bulgaria');
INSERT INTO Author (name, surname, birthDate, numberOfbooks, country) VALUES ('Carlie', 'Sikorski', '9/26/1919', 17, 'Serbia');
INSERT INTO Author (name, surname, birthDate, numberOfbooks, country) VALUES ('Enid', 'Boddis', '10/22/1918', 21, 'China');
INSERT INTO Author (name, surname, birthDate, numberOfbooks, country) VALUES ('Toiboid', 'Tassel', '9/4/1977', 23, 'Sweden');
INSERT INTO Author (name, surname, birthDate, numberOfbooks, country) VALUES ('Piotr', 'Cheetam', '10/5/1973', 22, 'Norway');

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
