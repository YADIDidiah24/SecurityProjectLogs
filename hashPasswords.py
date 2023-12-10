import sqlite3
import hashlib
import logging
from datetime import datetime
import pytz

def custom_time(record, datefmt='%Y-%m-%dT%H:%M:%S.%f%z'):
    timestamp = datetime.fromtimestamp(record.created, tz=pytz.timezone('Asia/Dubai'))
    return timestamp.strftime(datefmt)

# Set up authentication logger
auth_log = logging.getLogger('auth_logger')
auth_log.setLevel(logging.INFO)
auth_log_handler = logging.FileHandler('/var/log/auth.log')
auth_log_formatter = logging.Formatter('%(asctime)s kali %(levelname)s: %(message)s')
auth_log_formatter.datefmt = '%Y-%m-%dT%H:%M:%S.%f%z'
auth_log_formatter.formatTime = custom_time
auth_log_handler.setFormatter(auth_log_formatter)
auth_log.addHandler(auth_log_handler)

def hash_password(password):
    # Hash the password using SHA-256 
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    return hashed_password

current_time = datetime.now(pytz.timezone('Asia/Dubai')).strftime('%Y-%m-%dT%H:%M:%S.%f%z')

def create_user():
    username = input("Enter username: ")
    password = input("Enter password: ")

    # Hash the password
    hashed_password = hash_password(password)

    # Connect to the SQLite database
    conn = sqlite3.connect('user_credentials.db')  
    cursor = conn.cursor()

    try:
        # Insert the new user into the 'users' table with the hashed password
        cursor.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, hashed_password))
        conn.commit()

        # Log the new user creation and hashing
        auth_log_message = f'{current_time} NewUser-p: New User added, password hashed for {username}'
        auth_log.notice(auth_log_message)

    except sqlite3.IntegrityError:
        # Handle the case where the username already exists in the database
        auth_log.warning(f"{current_time} UserExists :Username '{username}' already exists. User creation failed.")

    finally:
        # Close the connection
        conn.close()

# Uncomment the following lines if you want to hash existing passwords
# def hash_existing_passwords():
#     conn = sqlite3.connect('user_credentials.db')  
#     cursor = conn.cursor()
# 
#     cursor.execute('SELECT id, password FROM users')
#     users = cursor.fetchall()
# 
#     for user in users:
#         user_id, original_password = user
#         hashed_password = hash_password(original_password)
#         cursor.execute('UPDATE users SET password = ? WHERE id = ?', (hashed_password, user_id))
# 
#     conn.commit()
#     conn.close()
# 
# hash_existing_passwords()

# Call the function to create a new user
create_user()
                  
