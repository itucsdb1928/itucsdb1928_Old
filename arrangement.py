import psycopg2
import psycopg2.extras


class Database:

    def __init__(self, dbname="d9ai7lm2fcpac2", user="actbkeboyhuxmt",
                 password="1fea78755cf3302bac2775a7084f213bde9769f6c1d416b9410f438158e584a3",
                 host="ec2-174-129-252-252.compute-1.amazonaws.com"):
        self.con = psycopg2.connect(database=dbname, user=user, password=password, host=host)
        self.cur = self.con.cursor()

    def get_home_page(self):
       with self.con.cursor(cursor_factory=psycopg2.extras.DictCursor) as cursor:
           query = "SELECT Books.Title,Author.name,Publisher.name FROM Books,Author,Publisher  WHERE Books.BookID=Publisher.PublisherID AND Books.BookID=Author.AuthorID"
           cursor.execute(query)
           playlists = cursor.fetchall()
           cursor.close()
         
       return playlists