import sqlite3

def CreateTable(): 
    conn = sqlite3.connect('User.db')
    # Create a cursor object using the connection
    cursor = conn.cursor()
    
    # Create a table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Users (
            Id Primary key,
            Username varchar(500),
            Password password,
            active BOOLEAN NOT NULL
        )
    ''')
    # Commit changes and close the connection
    conn.commit()
    conn.close()

def create_user(ID,Username, Password, active):
    conn = sqlite3.connect('User.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO Users (Username, Password, active) VALUES (?, ?,?,?)', (ID,Username, Password, active))
    conn.commit()
    conn.close()

def read_users():
    conn = sqlite3.connect('User.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Users')
    rows = cursor.fetchall()
    conn.close()
    return rows
    
def update_user(ID,Username, Password, active):
    conn = sqlite3.connect('User.db')
    cursor = conn.cursor()
    cursor.execute('UPDATE Users SET Username = ?, Password = ?, active = ? WHERE id = ?', (ID,Username, Password, active))
    conn.commit()
    conn.close()

def delete_user(Username):
    conn = sqlite3.connect('User.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM Users WHERE Username = ?', (Username,))
    conn.commit()
    conn.close()

# Example usage
# delete_user('Alice')
if __name__ == "__main__":
    # Create a table
    CreateTable()
    
    # Create Data in the table
    create_user(0,'Alice', 'Alice', True)
    create_user(1,'Sam', 'Sam', True)
    
    # Display Data in the Table
    users = read_users()
    for user in users:
        print(user)
    
    # UPdate Data in the Table
    update_user(0,'Alice Smith','Alice', True)
    
    # Delete Data From the Table.
    delete_user('Alice Smith')
