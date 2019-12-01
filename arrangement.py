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
           query = "SELECT Books.Title,Books.cover FROM Books,Author,Publisher  WHERE Books.PublisherID=Publisher.PublisherID AND Books.AuthorID=Author.AuthorID"
           cursor.execute(query)
           home = cursor.fetchall()
           cursor.close()
         
       return home

    def get_detail_page(self,book_name):
       with self.con.cursor(cursor_factory=psycopg2.extras.DictCursor) as cursor:
           query = "SELECT Author.name,Author.surname,Publisher.name,Books.PageNum FROM Books,Author,Publisher  WHERE Books.PublisherID=Publisher.PublisherID AND Books.AuthorID=Author.AuthorID AND Books.Title='%s'"%(book_name)
           cursor.execute(query)
           detail = cursor.fetchone()
           cursor.close()
         
       return detail

    def Search(self,name):
       with self.con.cursor(cursor_factory=psycopg2.extras.DictCursor) as cursor:
            query = "SELECT Books.Title FROM Books,Author,Publisher  WHERE Books.PublisherID=Publisher.PublisherID AND Books.AuthorID=Author.AuthorID AND Books.Title LIKE '%%%s%%' "%(name)
            cursor.execute(query)
            search = cursor.fetchall()
            cursor.close()
         
       return search

    def show_profile(self,UserId):
        with self.con.cursor(cursor_factory=psycopg2.extras.DictCursor) as cursor:
            query = "SELECT * FROM Users WHERE UserID={}".format(UserId)
            cursor.execute(query)
            profile = cursor.fetchall()
            cursor.close()
        return profile

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

