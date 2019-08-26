import sqlite3

connection = sqlite3.connect('data.db')

cursor = connection.cursor()

create_table = "CREATE TABLE users (id int, username text, password text)"
cursor.execute(create_table)

insert_query = "INSERT INTO users VALUES (1, 'ashraf', 'aaaa')"
cursor.execute(insert_query)

# insert many
users = [
    (2, 'ahmad', 'aaaa'),
    (3, 'amir', 'aaaa')
]
insert_query = "INSERT INTO users VALUES (?, ?, ?)"
cursor.executemany(insert_query, users)

# read
select_query = "SELECT * FROM users"
for row in cursor.execute(select_query):
    print(row)



connection.commit()
connection.close()
