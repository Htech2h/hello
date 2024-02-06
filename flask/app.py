from flask import Flask, render_template, request

app = Flask(__name__,template_folder='flask')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    # Check if the username and password are correct
    # If they are correct, redirect to the home page
    # If they are incorrect, show an error message
    return render_template('home.html', username=username,password=password)

if __name__ == '__main__':
    app.run(debug=True)
app.run(debug=True)