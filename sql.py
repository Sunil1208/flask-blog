import sqlite3

with sqlite3.connect("blog.db") as connection:

    # get a cursor object used to execute SQL commands
    c = connection.cursor()

    # create the table
    # c.execute("""CREATE TABLE posts
    #         (title TEXT, post TEXT)
    #         """)

    # insert dummy data into the table
    try:
        c.execute('INSERT INTO posts VALUES("Good", "I\'m good.")')
        c.execute('INSERT INTO posts VALUES("Well", "I\'m well.")')
        c.execute('INSERT INTO posts VALUES("Excellent", "I\'m excellent.")')
        c.execute('INSERT INTO posts VALUES("Okay", "I\'m okay.")')
    except sqlite3.OperationalError:
        print("Please check your SQL statements and try again")