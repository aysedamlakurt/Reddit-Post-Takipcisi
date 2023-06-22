import mysql.connector
import praw

config = {
    'user': 'root',
    'password': 'damlasude3',
    'host': 'localhost',
    'database': 'reddit_posts',
    'raise_on_warnings': True
}

 # MySQL sunucusuna bağlanma
try:
    conn = mysql.connector.connect(**config)
    print("Bağlantı başarılı")
except mysql.connector.Error as err:
    print("Hata:", err)



# Postu veritabanına ekleme işlevi
def postu_veritabanina_ekle(post):
    cursor = conn.cursor()

    # Veritabanına ekleme sorgusu
    query = "INSERT INTO posts (title, author) VALUES (%s, %s)"
    values = (post['title'], post['author'])
    
    try:
        cursor.execute(query, values)
        conn.commit()
        print("Post veritabanına eklendi")
    except mysql.connector.Error as err:
        print("Hata:", err)
        conn.rollback()

    cursor.close()



    
client_id = 'n4gZJg17Bj77PBwaz-6hBA'
client_secret = 'tGQEo3fbt_iWmr_DSOiRW3jJ-M2adA'
user_agent = 'post takipçisi/1.0 asdamlak'
username = 'asdamlak'


reddit = praw.Reddit(
    client_id=client_id,
    client_secret=client_secret,
    user_agent=user_agent,
    username=username,
    
)


subreddit = reddit.subreddit('bangtan')
posts = subreddit.new(limit=10)


    
for post in posts:
   for post in posts:
    print(post.title)
    # Post verilerini alarak veritabanına ekleme işlevini çağırma
    post_data = {
        'title': post.title,
        'author': post.author.name
    }
    postu_veritabanina_ekle(post_data)