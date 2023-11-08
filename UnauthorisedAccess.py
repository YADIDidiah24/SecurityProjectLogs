from flask import Flask, request
import logging
from datetime import datetime
from pytz import timezone

app = Flask(__name__)

def custom_time(record, datefmt='%Y-%m-%dT%H:%M:%S.%f%z'):
    timestamp = datetime.fromtimestamp(record.created, tz=timezone('Asia/Dubai'))
    return timestamp.strftime(datefmt)

auth_log = logging.getLogger('auth_logger')
auth_log.setLevel(logging.INFO)
auth_log_handler = logging.FileHandler('/var/log/auth.log')
auth_log_formatter = logging.Formatter('%(asctime)s kali %(message)s')
auth_log_formatter.datefmt = '%Y-%m-%dT%H:%M:%S.%f%z'
auth_log_formatter.formatTime = custom_time
auth_log_handler.setFormatter(auth_log_formatter)
auth_log.addHandler(auth_log_handler)

@app.route('/')
@app.route('/')
def index():
    login_form = '''
    <style>
        body {
            height: 100vh;
            background: red; /* Change the background color to red */
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
            <div class="title">NOTE: For Simulation Only!</div>
        </div>
    </div>
    '''
    return f'<html><body>{login_form}</body></html>'

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    # Get the current time
    current_time = datetime.now(timezone('Asia/Dubai')).strftime('%Y-%m-%dT%H:%M:%S.%f%z')

    # Check the credentials (in this example, we use a hardcoded valid username and password)
    valid_username = 'user1'
    valid_password = 'password123'

    if username == valid_username and password == valid_password:
        log_message = f'{current_time} kali SuccessfulLogin: Successful login for {username} from IP {request.remote_addr}'
        auth_log.info(log_message)
        return 'Login successful! YOU ARE AUTHORISED TO ACCESS THIS FILE! YAY'
    else:
        log_message = f'{current_time} kali UnauthorizedAccess: Unauthorized access attempt by {username} from IP {request.remote_addr}'
        auth_log.warning(log_message)
        return 'Login failed. YOU ARE NOT AUTHORISED TO ACCESS THIS FILE PLEASE GO BACK'

if __name__ == '__main__':
    app.run(port=8080)
                                                                                                                                                            

