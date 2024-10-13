import sqlite3

# Create a database connection
def create_db():
    conn = sqlite3.connect('users.db')  # Create a database file named 'users.db'
    cursor = conn.cursor()
    
    # Create users table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            username TEXT UNIQUE,
            password TEXT
        )
    ''')
    
    conn.commit()
    conn.close()

# Call this function once to create the database and table
create_db()
