from flask import Flask, request
import logging
from datetime import datetime
from pytz import timezone
from functools import wraps

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

html_style = 'text-align: center; background-color: red; font-size: 40px; font-weight: bold;'

username = ''
password = ''
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

    login_form = '''
    <style>
        body {
            height: 100vh;
            background: blue; 
            display: flex;
            justify-content: center;
            align-items: center;
            margin: 0;
        }

        .box {
            width: 300px;
            padding: 20px;
            background: #ffffff;
            border-radius: 10px;
            text-align: center;
        }

        #input[type="text"],
        #input[type="password"] {
            padding: 10px;
            font-size: 16px;
            border: 2px solid #ccc;
            border-radius: 5px;
            width: 100%;
        }

        #hhh {
            border: none;
            font-size: 16px;
            padding: 10px 20px;
            background-color: #febf00;
            color: #000;
            border-radius: 10px;
            cursor: pointer;
        }
    </style>
    <div class="box">
        <form method="post" action="/login">
            <h1 id="time">Login</h1>
            <input id="input" type="text" name="username" placeholder="Username" required><br><br>
            <input id="input" type="password" name="password" placeholder="Password" required><br><br>
            <button id="hhh" type="submit">Login</button>
        </form>
        <form method="get" action="/get_phrase">
            <button id="hhh" type="submit">Get Today's Phrase</button>
        </form>
        <div class="card">
            <div class="title">NOTE: For Simulation Only!</div>
        </div>
    </div>
    '''
    return f'<html><body>{login_form}</body></html>'

@app.route('/login', methods=['POST'])
def login():
    global username, password
    username = request.form['username']
    password = request.form['password']

    # Get the current time
    current_time = datetime.now(timezone('Asia/Dubai')).strftime('%Y-%m-%dT%H:%M:%S.%f%z')

    # Check the credentials (in this example, we use a hardcoded valid username and password)
    valid_username = ['user123',"admin"]
    valid_password = 'password123'

    if username in valid_username and password == valid_password:
        # Authentication successful
        auth_log_message = f'{current_time} kali SuccessfulLogin: Successful login for {username} from IP {request.remote_addr}'
        auth_log.info(auth_log_message)
        return f'<html><body style="{html_style}">Login successful! YOU ARE LOGGED IN !!</body></html>',200

    else:
        session_log_message = f'{current_time} kali FailedLogin: Failed login attempt for user {username} from IP {request.remote_addr}'
        session_log.warning(session_log_message)

        return f'<html><body style="{html_style}">Login failed. INVALID CREDENTIALS</body></html>', 401

@app.route('/get_phrase', methods=['GET'])
def get_phrase():
    global username
    global password
    # Get the current time
    current_time = datetime.now(timezone('Asia/Dubai')).strftime('%Y-%m-%dT%H:%M:%S.%f%z')
    session_log_message = f'{current_time} Session: User accessed get_phrase from IP {request.remote_addr}'
    session_log.info(session_log_message)

    valid_username = "admin"
    valid_password = 'password123'

    if username == valid_username and password == valid_password:
        # Authorized access
        auth_log_message = f'{current_time} kali AuthorizedAccess: Authorized access for user1 from IP {request.remote_addr}'
        auth_log.info(auth_log_message)

        return f'<html><body style="{html_style}">Today\'s Phrase: You are authorized to access this information!</body></html>', 200

    else:
        # Unauthorized access
        auth_log_message = f'{current_time} kali UnauthorizedAccess: Unauthorized access attempt from IP {request.remote_addr}'
        auth_log.warning(auth_log_message)

        return f'<html><body style="{html_style}">Unauthorized access. You are not authorized to access this information.</body></html>', 401

if __name__ == '__main__':
    app.run(port=9080)
                                                                                                                                                                                                                                           
