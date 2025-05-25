from flask import Flask, render_template, request
import psycopg2

app = Flask(__name__)

# Database connection
def get_db_connection():
    conn = psycopg2.connect(
        host='dpg-d0pj1qodl3ps73argvhg-a',
        database='cloud_lab_8br0',
        user='cloud_lab_8br0_user',
        password='McBRr8DyPse7bAX7B3bzBTbWaoXNtOnt'
    )
    return conn

# Root URL renders the form
@app.route('/', methods=['GET'])
def index():
    return render_template('task3_validate_user.html')

# Handles form submission
@app.route('/validate_user', methods=['POST'])
def validate_user():
    username = request.form['username']
    password = request.form['password']

    # Insert user data into PostgreSQL
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS users (username VARCHAR(50), password VARCHAR(50));")
    cur.execute("INSERT INTO users (username, password) VALUES (%s, %s);", (username, password))
    conn.commit()
    cur.close()
    conn.close()

    return 'User validated and stored in the database.'

if __name__ == '__main__':
    app.run(debug=True)
