from flask import Flask, request
import logging

app = Flask(__name__)

# Configure the logger to write to the auth.log file
auth_log = logging.getLogger('auth_logger')
auth_log.setLevel(logging.INFO)
auth_log_handler = logging.FileHandler('/var/log/auth.log')
auth_log_formatter = logging.Formatter('Failed login attempt for user %(username)s from IP %(ip_address)s: %(reason)s')
auth_log_handler.setFormatter(auth_log_formatter)
auth_log.addHandler(auth_log_handler)

@app.route('/')
def index():
    login_form = '''
    <div class="box">
        <form method="post" action="/login">
            <h1 id="time">Login</h1>
            <input id="input" type="text" name="username" placeholder="Username" required><br><br>
            <input id="input" type="password" name="password" placeholder="Password" required><br><br>
            <button id="hhh" type="submit">Login</button>
        </form>
        <div class="card">
            <div class="title">Your Additional Content Here</div>
        </div>
    </div>
    '''
    return login_form

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    # Check the credentials (in this example, we use a hardcoded valid username and password)
    valid_username = 'admin'
    valid_password = 'password123'

    if username == valid_username and password == valid_password:
        auth_log.info(f'Successful login for user {username}')
        return 'Login successful!'
    else:
        # Log the failed login attempt with the custom format
        auth_log.warning(f'Failed login attempt for user {username} from IP {request.remote_addr}: Incorrect password')
        return 'Login failed. Please check your credentials.'

if __name__ == '__main__':
    app.run()
from flask import Flask, request
import logging
from datetime import datetime

app = Flask(__name__)

def custom_time(record, datefmt='%b %d %H:%M:%S %Y'):
    timestamp = record.created
    return datetime.fromtimestamp(timestamp).strftime(datefmt)

auth_log = logging.getLogger('auth_logger')
auth_log.setLevel(logging.INFO)
auth_log_handler = logging.FileHandler('/var/log/auth.log')
auth_log_formatter = logging.Formatter('%(message)s', datefmt='%b %d %H:%M:%S %Y')
auth_log_formatter.formatTime = custom_time  # Use the custom_time function to format the timestamp
auth_log_handler.setFormatter(auth_log_formatter)
auth_log.addHandler(auth_log_handler)

# Configure the logger to write to the auth.log file
auth_log = logging.getLogger('auth_logger')
auth_log.setLevel(logging.INFO)
auth_log_handler = logging.FileHandler('/var/log/auth.log')
auth_log_formatter = logging.Formatter('%(b)s %(d)s %(H)s:%(M)s:%(S)s %Y')
auth_log_handler.setFormatter(auth_log_formatter)
auth_log.addHandler(auth_log_handler)

@app.route('/')
def index():
    login_form = '''
    <style>
        body {
            height: 100vh;
            background: linear-gradient(135deg, #8052ec, #d161ff);
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
        <div class="card">
            <div class="title">Your Additional Content Here</div>
        </div>
    </div>
    '''
    return f'<html><body>{login_form}</body></html>'

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    # Get the current time
    current_time = datetime.now().strftime('%b %d %H:%M:%S')

    # Check the credentials (in this example, we use a hardcoded valid username and password)
    valid_username = 'admin'
    valid_password = 'password123'

    if username == valid_username and password == valid_password:
        log_message = f'{current_time} Successful login for user {username}'
        auth_log.info(log_message)
        return 'Login successful!'
    else:
        log_message = f'{current_time} Failed login attempt for user {username} from IP {request.remote_addr}: Incorrect password'
        auth_log.warning(log_message)
        return 'Login failed. Please check your credentials.'

if __name__ == '__main__':
    app.run()
                                                                                                                                                                                                                                           
