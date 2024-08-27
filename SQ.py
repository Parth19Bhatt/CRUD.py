import sqlite3
def CreateTable(): 
    conn = sqlite3.connect('User.db')

    # Create a cursor object using the connection
    cursor = conn.cursor()
    
    # Create a table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Users (
            Username varchar(500),
            Password Hash password,
            active BOOLEAN NOT NULL
        )
    ''')
    
    # Commit changes and close the connection
    conn.commit()
    conn.close()

def create_user(Username, Password, active):
    conn = sqlite3.connect('User.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO Users (Username, Password, active) VALUES (?, ?)', (Username, Password, active))
    conn.commit()
    conn.close()

# Example usage
create_user('Alice', 'Alice', True)
def read_users():
    conn = sqlite3.connect('User.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Users')
    rows = cursor.fetchall()
    conn.close()
    return rows

# Example usage
users = read_users()
for user in users:
    print(user)
    
def update_user(Username, Password, active):
    conn = sqlite3.connect('User.db')
    cursor = conn.cursor()
    cursor.execute('UPDATE Users SET name = ?, age = ? WHERE id = ?', (Username, Password, active))
    conn.commit()
    conn.close()

# Example usage
update_user('Alice Smith','Alice', True)

def delete_user(Username):
    conn = sqlite3.connect('User.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM Users WHERE id = ?', (Username,))
    conn.commit()
    conn.close()

# Example usage
delete_user('Alice')


if __name__ == '__main__':
    # CreateTable("User.db")
    CreateTable()
    # create_user()
    # read_users()