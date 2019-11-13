import psycopg2
import psycopg2.extras


class Database:
    def __init__(self, dbname="d9qfricrmj8vii", user="tnivydbyztjmgh",	 
                    password="b791cb0275732cebe4b23d3ce0d53d0d4a308966829b297983dafc39553f170a",	
                    host="ec2-174-129-41-127.compute-1.amazonaws.com"):
        self.con = psycopg2.connect(database=dbname, user=user, password=password, host=host)
        self.cur = self.con.cursor()
    
    def get_home_page(self):
       with self.con.cursor(cursor_factory=psycopg2.extras.DictCursor) as cursor:
           query = "SELECT Books.Title,Author.name,Publisher.name FROM Books,Author,Publisher  WHERE Books.BookID=Publisher.PublisherID AND Books.BookID=Author.AuthorID"
           cursor.execute(query)
           playlists = cursor.fetchall()
           cursor.close()
         
       return playlists

    def checkLogin(self,email,password):
       UserID = 0
       info = []
       with self.con.cursor(cursor_factory=psycopg2.extras.DictCursor) as cursor:
           query = "SELECT UserID ,email,password FROM Users WHERE email='%s' and password = '%s';" %(email,password)
           cursor.execute(query)
           info = cursor.fetchone()
           if info is not None:
               UserID = info[0]

       return UserID


    def insertNewUser(self,form):
        with self.con.cursor(cursor_factory=psycopg2.extras.DictCursor) as cursor:
            query = "select email from users where email = '%s';" %(form.email.data)
            cursor.execute(query)
            info = cursor.fetchone()

        if info is None:
            with self.con.cursor(cursor_factory=psycopg2.extras.DictCursor) as cursor:
                query = "INSERT INTO Users (name,surname,gender,age,email,password,isAdmin) VALUES ('%s','%s','%s','%s','%s', '%s',0);" %(form.name.data,form.surname.data,form.gender.data,form.age.data,form.email.data,form.password.data)
                cursor.execute(query)
  
            with self.con.cursor(cursor_factory=psycopg2.extras.DictCursor) as cursor:
                query = "SELECT UserID  FROM Users WHERE email='%s';" %(form.email.data)
                cursor.execute(query)
                info = cursor.fetchone()
                return info[0]
    
        return 0