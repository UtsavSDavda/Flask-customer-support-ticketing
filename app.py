from flask import Flask, render_template, request, redirect, session
import boto3

app = Flask(__name__)
app.secret_key = 'Gojo@Topi31'

# Connect to DynamoDB
dynamodb = boto3.resource('dynamodb', region_name='your_region')
table = dynamodb.Table('your_table_name')
# Routes
@app.route('/')
def index():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    # Check if user exists and password matches
    response = table.get_item(Key={'username': username})
    if 'Item' in response:
        user_data = response['Item']
        if user_data['password'] == password:
            session['username'] = username
            return redirect('/dashboard') 
    return 'Invalid username or password'

@app.route('/dashboard')
def dashboard():
    if 'username' in session:
        return 'Welcome, ' + session['username'] + '!'
    else:
        return redirect('/')

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
