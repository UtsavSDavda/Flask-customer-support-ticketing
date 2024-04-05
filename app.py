from flask import Flask, request, render_template, redirect, url_for, session
import pymysql.cursors

app = Flask(__name__)

# RDS configuration
rds_host = 'flask-cs.cdc4ya0a6v85.ap-southeast-2.rds.amazonaws.com'
username = 'admin'
password = 'sBb9BByydbcV5aAYdU4y'
db_name = 'your-database-name'

# Connect to the database
connection = pymysql.connect(host=rds_host,
                             user=username,
                             password=password,
                             db=db_name,
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

@app.route('/')
def index():
    # Retrieve ticket data from the database
    with connection.cursor() as cursor:
        sql = "SELECT * FROM tickets"
        cursor.execute(sql)
        tickets = cursor.fetchall()

    return render_template('index.html', tickets=tickets)
def user_login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        # Check credentials
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM users WHERE username=%s AND password=%s', (username, password))
        user = cursor.fetchone()
        cursor.close()
        
        if user:
            session['username'] = username
            return redirect(url_for('index'))
        else:
            return 'Invalid username or password'

    return render_template('login.html')

'''
@app.route('/raiser')
def raise_ticekt():
    with connection.cursor as cursor:
        sql = ""
        cursor.execute(sql)
    return render_template('customer_response.html')
'''


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=False) # Run the app in production mode
