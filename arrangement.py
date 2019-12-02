import psycopg2
import psycopg2.extras


class Database:
    def __init__(self, dbname="d9qfricrmj8vii", user="tnivydbyztjmgh",	 
                    password="b791cb0275732cebe4b23d3ce0d53d0d4a308966829b297983dafc39553f170a",	
                    host="ec2-174-129-41-127.compute-1.amazonaws.com"):
        self.con = psycopg2.connect(database=dbname, user=user, password=password, host=host)
        self.cur = self.con.cursor()
        self.UserId = 0
        self.book_name = None
        self.book_detail = None
    
    def get_home_page(self):
       with self.con.cursor(cursor_factory=psycopg2.extras.DictCursor) as cursor:
           query = "SELECT Books.Title,Books.content FROM Books,Author,Publisher  WHERE Books.PublisherID=Publisher.PublisherID AND Books.AuthorID=Author.AuthorID"
           cursor.execute(query)
           home = cursor.fetchall()
         
       return home

    def get_detail_page(self,book_name):
       with self.con.cursor(cursor_factory=psycopg2.extras.DictCursor) as cursor:
           query = "SELECT Author.name,Author.surname,Publisher.name,Books.PageNum,Books.BookRewiev,Books.BookID FROM Books,Author,Publisher  WHERE Books.PublisherID=Publisher.PublisherID AND Books.AuthorID=Author.AuthorID AND Books.Title='%s'"%(book_name)
           cursor.execute(query)
           detail = cursor.fetchone()
         
       return detail

    def Search(self,name):
       with self.con.cursor(cursor_factory=psycopg2.extras.DictCursor) as cursor:
            query = "SELECT Books.Title FROM Books,Author,Publisher  WHERE Books.PublisherID=Publisher.PublisherID AND Books.AuthorID=Author.AuthorID AND Books.Title LIKE '%%%s%%' "%(name)
            cursor.execute(query)
            search = cursor.fetchall()
         
       return search

    def show_profile(self,UserId):
        with self.con.cursor(cursor_factory=psycopg2.extras.DictCursor) as cursor:
            query = "SELECT * FROM Users WHERE UserID={}".format(UserId)
            cursor.execute(query)
            profile = cursor.fetchall()

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

    def insertRate(self,userId,bookId,form):
        info = None
        with self.con.cursor(cursor_factory=psycopg2.extras.DictCursor) as cursor:
           query = "INSERT INTO bookrewiev (UserID,BookID,UserRating,UserComment) VALUES (%s, %s ,%s,'%s');" %(userId,bookId,form['optradio'],form['comment'])
           cursor.execute(query)
           return True

        return False

    def checkUser(self,userId,bookId):
        info = None
        with self.con.cursor(cursor_factory=psycopg2.extras.DictCursor) as cursor:
            query = "SELECT userid FROM bookrewiev where userid = '%d' and bookid = %d" %(userId,bookId)
            cursor.execute(query)
            info = cursor.fetchone()
        if info is None:
            return True
        
        return False


    def getRateInfo(self,bookId):
        info = None
        sum = 0
        avg = 0
        rates = {1:[0,0],2:[0,0],3:[0,0],4:[0,0],5:[0,0]}
        with self.con.cursor(cursor_factory=psycopg2.extras.DictCursor) as cursor:
            query = "SELECT userrating from bookrewiev WHERE bookid = %d" %(bookId)
            cursor.execute(query)
            info = cursor.fetchall()

        for i in info:
          sum += i[0]
          rates[i[0]][0] += 1
        
        voteNum = len(info)
        for i in range(1,6):
            if(voteNum):
                rates[i][1] = int((rates[i][0] / voteNum)*100)
            else:
                rates[i][1] = 0
        
        if voteNum: avg = (sum / voteNum)

        return (avg,int(avg),voteNum,rates)