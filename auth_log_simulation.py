from flask import Flask, request, g
import logging
from datetime import datetime
from pytz import timezone
from functools import wraps
import hashlib
import sqlite3

app = Flask(__name__)

def custom_time(record, datefmt='%Y-%m-%dT%H:%M:%S.%f%z'):
    timestamp = datetime.fromtimestamp(record.created, tz=timezone('Asia/Dubai'))
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

# Set up session logger using the same file handler and formatter
session_log = logging.getLogger('session_logger')
session_log.setLevel(logging.INFO)
session_log_handler = logging.FileHandler('/var/log/auth.log')  # Use the same handler as auth_log
session_log_handler.setFormatter(auth_log_formatter)  # Use the same formatter as auth_log
session_log.addHandler(session_log_handler)

# Set up error logger using the same file handler and formatter
error_log = logging.getLogger('error_logger')
error_log.setLevel(logging.ERROR)
error_log_handler = logging.FileHandler('/var/log/auth.log')  # Use the same handler as auth_log
error_log_handler.setFormatter(auth_log_formatter)  # Use the same formatter as auth_log
error_log.addHandler(error_log_handler)

def hash_password(password):
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    return hashed_password
DATABASE = 'user_credentials.db'

# Function to get the database connection
def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

# Function to execute a query and return results
def execute_query(query, parameters=(), fetchone=False):
    with app.app_context():
        db = get_db()
        cursor = db.cursor()
        cursor.execute(query, parameters)

        if fetchone:
            result = cursor.fetchone()
        else:
            result = cursor.fetchall()

        cursor.close()
        db.commit()

    return result

username = ''
password = ''

common_styling = '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <title>{title}</title>
        <!-- Stylesheet -->
        <style media="screen">
            body {{
                background-color: {background_color};
                font-family: 'Poppins', sans-serif;
                text-align: center;
            }}
            .container {{
                margin-top: 50px;
                padding: 20px;
                background-color: #fff;
                border-radius: 10px;
                box-shadow: 0 0 20px rgba(0, 0, 0, 0.1);
            }}
            h1 {{
                color: #1e1a36;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <h1>{message}</h1>
        </div>
    </body>
    </html>
'''

def log_request_info(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        current_time = datetime.now(timezone('Asia/Dubai')).strftime('%Y-%m-%dT%H:%M:%S.%f%z')
        request_info = f'{current_time} IncomingRequest: {request.method} {request.path} from IP {request.remote_addr}'
        session_log.info(request_info)
        return func(*args, **kwargs)

    return wrapper

@app.route('/')
@log_request_info
def index():
    # Log session when user accesses the website
    current_time = datetime.now(timezone('Asia/Dubai')).strftime('%Y-%m-%dT%H:%M:%S.%f%z')
    session_log_message = f'{current_time} Session: User accessed the website from IP {request.remote_addr}'
    session_log.info(session_log_message)

    html = '''
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <title>Login</title>
            <!--Stylesheet-->
        <style media="screen">

            *:after{
                padding: 0;
                margin: 0;
                box-sizing: border-box;
            }
            body{
                background-color: #1e1a36;
            }
            .background{
                width: 430px;
                height: 520px;
                position: absolute;
                transform: translate(-50%,-50%);
                left: 50%;
                top: 50%;
            }
            .background .shape{
                height: 200px;
                width: 200px;
                position: absolute;
                border-radius: 50%;
            }
            .shape:first-child{
                background: linear-gradient(
                    #57dd09,
                    #23a2f6
                );
                left: -110px;
                top: -110px;
            }
            .shape:last-child{
                background: linear-gradient(
                    to right,
                    #fc2c03,
                    #f09819
                );
                right: -110px;
                bottom: -110px;
            }
            form{
                height: 470px;
                width: 380px;
                background-color: rgba(7, 0, 0, 0.13);
                position: absolute;
                transform: translate(-50%,-50%);
                top: 50%;
                left: 50%;
                border-radius: 10px;
                backdrop-filter: blur(10px);
                border: 2px solid rgba(241, 235, 235, 0.1);
                box-shadow: 0 0 40px rgba(145, 143, 160, 0.6);
                padding: 50px 35px;
            }
            form *{
                font-family: 'Poppins',sans-serif;
                color: #cac8c8;
                letter-spacing: 0.5px;
                outline: none;
                border: none;
            }
            form h3{
                font-size: 32px;
                font-weight: 500;
                line-height: 42px;
                text-align: center;
            }

            label{
                display: block;
                margin-top: 30px;
                font-size: 16px;
                font-weight: 500;
            }
            input{
                display: block;
                height: 50px;
                width: 100%;
                background-color: rgba(247, 239, 239, 0.411);
                border-radius: 3px;
                padding: 0px 0px;
                margin-top: 8px;
                font-size: 14px;
                font-weight: 300;
                text-indent: 10px;
            }
            ::placeholder{
                color: #e0d9d9;
            }

            button{
                margin-top: 30px;
                width: 100%;
                background-color: #d6cfcf;
                color: #080710;
                padding: 15px 0px;
                font-size: 18px;
                font-weight: 600;
                border-radius: 5px;
                cursor: pointer;
            }

            #change{
                display: inline-block;
                margin-top: 20px;
                width: 50%;
                background-color: #949292;
                color: #232324;
                padding: 8px 0;
                font-size: 14px;
                font-weight: 600;
                border-radius: 5px;
                cursor: pointer;
            }
            .social div{
            background: red;
            width: 150px;
            border-radius: 3px;
            padding: 5px 10px 10px 5px;
            background-color: rgba(255,255,255,0.27);
            color: #eaf0fb;
            text-align: center;
            }
            .social div:hover{
            background-color: rgba(255,255,255,0.47);
            }
            .social .fb{
            margin-left: 25px;
            }
            .social i{
            margin-right: 4px;
            }
            .button-container {
                display: flex;
                gap: 10px;
            }
            .button-container button {
                backdrop-filter: none;
            }

        </style>
        </head>
        <body>
            <div class="background">
                <div class="shape"></div>
                <div class="shape"></div>
            </div>
            <form method="post" action="/process">
                <h3>Authenticate Here</h3>

                <label for="username">Username</label>
                <input type="text" placeholder="Enter Username" id="username" name="username">

                <label for="password">Password</label>
                <input type="password" placeholder="Enter Password" id="password" name="password">

                <button type="submit" name="action" value="login">Log In</button>
                <div class="button-container">
                    <button type="submit" name="action" value="changePassword">Change Password</button>
                    <button type="submit" name="action" value="onlyAuthorised">Only Authorised</button>
                </div>
                <p>Note: For Simulation Only</p>

            </form>
        </body>
        </html>
    '''
    return html

@app.route('/process', methods=['POST'])
def process_form():
    action = request.form.get('action')

    if action == 'login':
        return login()
    elif action == 'changePassword':
        return change_password()
    elif action == 'onlyAuthorised':
        return only_authorized()
    else:
        return "Invalid action"

def login():
    global username, password
    username = request.form['username']
    password = request.form['password']

    # Get the current time
    current_time = datetime.now(timezone('Asia/Dubai')).strftime('%Y-%m-%dT%H:%M:%S.%f%z')

    # Hash the provided password
    hashed_password = hash_password(password)

    # Check the credentials against the database
    query = "SELECT * FROM users WHERE username=?"
    user = execute_query(query, (username,), fetchone=True)

    if user and user[2] == hashed_password:  # Assuming hashed password is stored in the third column
        # Authentication successful
        auth_log_message = f'{current_time} kali SuccessfulLogin: Successful login for {username} from IP {request.remote_addr}'
        auth_log.info(auth_log_message)
        styled_html = common_styling.format(title='Login Successful', background_color='#42f590', message=f'Hello {username}! Login successful! YOU ARE LOGGED IN !!')

        return styled_html, 200
    else:
        session_log_message = f'{current_time} kali FailedLogin: Failed login attempt for user {username} from IP {request.remote_addr}'
        session_log.warning(session_log_message)
        styled_html = common_styling.format(title='Login Failed', background_color='#fc1303', message=f'{username} your Login has failed. INVALID CREDENTIALS')

        return styled_html, 401

def change_password():
    # Implement your change password logic here
    return "Change Password logic goes here"

def only_authorized():
    global username, password

    # Get the current time
    current_time = datetime.now(timezone('Asia/Dubai')).strftime('%Y-%m-%dT%H:%M:%S.%f%z')
    session_log_message = f'{current_time} Session: User accessed only_authorized from IP {request.remote_addr}'
    session_log.info(session_log_message)

    valid_username = "admin"
    valid_password = 'password123'

    if username == valid_username and password == valid_password:
        # Authorized access
        auth_log_message = f'{current_time} kali AuthorizedAccess: Authorized access for User {username} from from IP {request.remote_addr}'
        auth_log.info(auth_log_message)
        styled_html = common_styling.format(title='Authorized Access', background_color='#0307fc', message=f'{username} you are Authorized to Access this information.(GOOD LUCK)')

        return styled_html, 200

    else:
        # Unauthorized access
        auth_log_message = f'{current_time} kali UnauthorizedAccess: Unauthorized access attempt from User {username} from IP {request.remote_addr}'
        auth_log.warning(auth_log_message)
        styled_html = common_styling.format(title='Unauthorized Access', background_color='#fcdf03', message=f'{username} you are not Authorized to Access this information. (GO BACK)')

        return styled_html, 200
if __name__ == '__main__':
    app.run(port=9080)
