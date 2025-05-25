from flask import Flask, request, redirect
import psycopg2

app = Flask(__name__)

# PostgreSQL connection
db = psycopg2.connect(
    host='dpg-d0pj1qodl3ps73argvhg-a',
        database='cloud_lab_8br0',
        user='cloud_lab_8br0_user',
        password='McBRr8DyPse7bAX7B3bzBTbWaoXNtOnt',
    port=5432
)
cursor = db.cursor()

# Create users table
cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        username VARCHAR(50),
        password VARCHAR(50)
    );
""")
db.commit()

# Common CSS
HTML_STYLE = """
<style>
    body { font-family: Arial, sans-serif; background-color: #f0f2f5; text-align: center; margin-top: 50px; }
    h2 { color: #333; }
    form, .box { display: inline-block; padding: 20px; background: #fff; border-radius: 8px; box-shadow: 0 0 10px rgba(0,0,0,0.1); }
    input { margin: 10px 0; padding: 8px; width: 90%; border: 1px solid #ccc; border-radius: 4px; }
    input[type="submit"], button { background-color: #007bff; color: white; border: none; padding: 8px 16px; border-radius: 4px; cursor: pointer; }
    input[type="submit"]:hover, button:hover { background-color: #0056b3; }
    .note { margin-top: 20px; font-size: 14px; color: #555; }
</style>
"""

# Register page (GET)
@app.route('/')
def index():
    return HTML_STYLE + '''
    <div class="box">
        <h2>Register</h2>
        <form action="/register" method="post">
            <input name="username" placeholder="Username" required><br>
            <input name="password" type="password" placeholder="Password" required><br>
            <input type="submit" value="Register">
        </form>
        <p>Already registered? <a href="/login">Login here</a></p>
    </div>
    '''

# Login page (GET)
@app.route('/login')
def login_page():
    return HTML_STYLE + '''
    <div class="box">
        <h2>Login</h2>
        <form action="/login" method="post">
            <input name="username" placeholder="Username" required><br>
            <input name="password" type="password" placeholder="Password" required><br>
            <input type="submit" value="Login">
        </form>
    </div>
    '''

# Register (POST)
@app.route('/register', methods=['POST'])
def register():
    username = request.form['username']
    password = request.form['password']
    cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, password))
    db.commit()
    return redirect("/login")

# Login (POST)
@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    cursor.execute("SELECT * FROM users WHERE username=%s AND password=%s", (username, password))
    user = cursor.fetchone()
    if user:
        return HTML_STYLE + '''
        <h2>✅ Login Successful</h2>
        <a href="/login"><button>Back</button></a>
        '''
    else:
        return HTML_STYLE + '''
        <h2>❌ Login Failed</h2>
        <a href="/login"><button>Back</button></a>
        '''

# Start the server
if __name__ == '__main__':
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
