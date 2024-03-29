-------------------------------------------------------
NEW

    CREATE TABLE Author( 
                      AuthorID SERIAL PRIMARY KEY , 
                      name VARCHAR(30), 
                      surname VARCHAR(30),
                      birthDate TIME , 
                      numberOfbooks INTEGER,
                      country VARCHAR(20)
                     );
    CREATE TABLE BookRewiev( 
                      BookRewievID SERIAL PRIMARY KEY ,
                      review INTEGER,
                      PostDate TIME,
                      UserRating INTEGER,
                      lostEdit VARCHAR(50),
                      orginalText VARCHAR(100) 
                     );
                     
    CREATE TABLE Publisher( 
                      PublisherID SERIAL PRIMARY KEY , 
                      name VARCHAR(40), 
                      adress VARCHAR(50),
                      numberOfbooks INTEGER , 
                      establishmentDate TIME ,
                      logo VARCHAR(50)
                     );
                     
    CREATE TABLE Books( 
                      BookID SERIAL PRIMARY KEY , 
                      Title VARCHAR(20),
                      PageNum INTEGER,
                      BookRewiev INTEGER REFERENCES BookRewiev (BookRewievID) , 
                      PublisherID INTEGER REFERENCES Publisher (PublisherID), 
                      AuthorID INTEGER REFERENCES Author (AuthorID) ,
                      cover VARCHAR(50)
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
                      name VARCHAR (50) UNIQUE NOT NULL, 
                      surname VARCHAR (50) UNIQUE NOT NULL, 
                      gender VARCHAR (6) NULL, 
                      age VARCHAR (3) NULL,
                      content INTEGER REFERENCES UserContent (UserContentID),
                      email VARCHAR (50) UNIQUE NOT NULL,
                      password VARCHAR (20) UNIQUE NOT NULL,
                      isAdmin INTEGER
                     );
---------------------------------------------------------
OLD


CREATE TABLE Users( 
                  UserID SERIAL PRIMARY KEY REFERENCES Account (AccountId), 
                  name VARCHAR (50) UNIQUE NOT NULL, 
                  surname VARCHAR (50) UNIQUE NOT NULL, 
                  gender VARCHAR (6) NULL , 
                  age VARCHAR (3) NULL ,
                  isAdmin VARCHAR (3) NULL      
                 );
CREATE TABLE Admin( 
                  AdminID SERIAL PRIMARY KEY REFERENCES Account (AccountId), 
                  HesapSahibi VARCHAR (60) UNIQUE NOT NULL, 
                  HesapTipi VARCHAR (50) UNIQUE NOT NULL, 
                  Iban VARCHAR (30) NULL , 
                  Sube VARCHAR (30) NULL                 
                 );  
CREATE TABLE CreditCard( 
                  CreditCardID SERIAL PRIMARY KEY , 
                  UserID INTEGER REFERENCES Users (UserID), 
                  CrediCardNum VARCHAR (30) UNIQUE NULL, 
                  CrediCardName VARCHAR (30) NULL , 
                  CrediCardDate TIME                 
                 );
CREATE TABLE AdminContent( 
                  AdminContentID SERIAL PRIMARY KEY , 
                  Title VARCHAR(30) UNIQUE NOT NULL  , 
                  Price NUMERIC(4,2), 
                  IssuaDate TIME , 
                  PageNum INTEGER                
                 );
CREATE TABLE UserContent( 
                  UserContentID SERIAL PRIMARY KEY , 
                  Vote INTEGER, 
                  VoteNum INTEGER, 
                  Score FLOAT , 
                  Comments VARCHAR(200)                
                 );
CREATE TABLE Publisher( 
                  PublisherID SERIAL PRIMARY KEY , 
                  name VARCHAR(40), 
                  adress VARCHAR(50),
                  numberOfbooks INTEGER , 
                  establishmentDate TIME               
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
                  AdminContentID INTEGER REFERENCES AdminContent (AdminContentID) , 
                  UserContentID INTEGER REFERENCES UserContent (UserContentID) , 
                  PublisherID INTEGER REFERENCES Publisher (PublisherID), 
                  AuthorID INTEGER REFERENCES Author (AuthorID)               
                 );   
CREATE TABLE Orders( 
                  OrdersID SERIAL PRIMARY KEY , 
                  UserID INTEGER REFERENCES Users (UserID), 
                  BookID INTEGER REFERENCES Books  (BookID), 
                  TotalAmount NUMERIC(4,2), 
                  OrderStatusID INTEGER,
                  OrderAdress INTEGER,
                  BillingAdress INTEGER
                 ); 
CREATE TABLE OrderStatus( 
                  OrderStatusID SERIAL PRIMARY KEY REFERENCES Orders (OrdersID), 
                  Statu VARCHAR(10), 
                  CargoName VARCHAR(20), 
                  TrackingNumber INTEGER, 
                  SendTime TIME
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
          

 


