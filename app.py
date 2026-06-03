# from flask import Flask, render_template # <--- render_template ko yahan add karo

# app = Flask(__name__)

# #ye tumhara homepage hai
# @app.route('/')
# def home():
#     # Ab ye "homepage.html" ko templates folder mein dhundega
#     return render_template('homepage.html')

# # Ye mera login page ka rasta hai
# @app.route('/login')
# def login_page():
#     # Ab ye "Login.html" ko templates folder mein dhundega
#     return render_template('Login.html')

# if __name__ == '__main__':
#     app.run(debug=True)  

# New code for catch the data : 
# from flask import Flask, render_template, request  # 1. 'request' ko add kiya data lene ke liye

# app = Flask(__name__)

# @app.route('/')
# def home():
#     return render_template('homepage.html')

# # 2. 'methods' mein GET aur POST dono dale hain
# @app.route('/login', methods=['GET', 'POST'])
# def login_page():
#     if request.method == 'POST':
#         # 3. HTML ke 'name' attribute se data nikal rahe hain
#         user = request.form.get('username')
#         ip = request.form.get('server_ip') 
        
#         # 4. Ye tumhare VS Code ke Terminal mein dikhega
#         # print(f"\n--- Data Received from Frontend ---")
#         # print(f"Username: {user}")
#         # print(f"IP Address: {ip}")
#         # print(f"-----------------------------------\n")

    #     # Terminal mein check krne k liye print kro
    #     print("REACHED INSIDE LOGIN ROUTE")
    #     print(f"User {user} is logging in for server: {ip}")

    #     # Yaha 'dashboard.html' ko link kar rhe hain
    #     # Hum 'username' aur 'ip' ko variable ke roop mein bhej rhe hai
    #     return render_template('dashboard.html', username=user, ip=ip, metrics={})
        
    #     # return f"<h1>Success!</h1><p>'{user}' aur IP '{ip}'!</p>"

    # # Agar user sirf page visit kar raha hai (GET), toh login form dikhao 
#     return render_template('Login.html')

# if __name__ == '__main__':
#     app.run(debug=True)  


# new updated app.py by G
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

# --- Database Configuration ---
# This creates a 'cloudvitals.db' file in your project folder
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cloudvitals.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'cloudvitals_key_2026' 

db = SQLAlchemy(app)

# --- User Database Model ---
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    server_ip = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(200), nullable=False)
    #email = db.Column(db.String(200), nullable=False)

# Create the database file automatically if it doesn't exist
with app.app_context():
    db.create_all()

# --- Routes ---

@app.route('/')
def home():
    return render_template('homepage.html')

# 1. Signup Route: For new users to "Create Account"
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        user = request.form.get('username')
        # ip = request.form.get('server_ip')
        email = request.form.get('email')
        pwd = request.form.get('password')
        

        # Check if username is already taken
        existing_user = User.query.filter_by(username=user).first()
        if existing_user:
            return "<h1>Error!</h1><p>Username already exists. Please choose another.</p>"

        # Save new user with a secure hashed password
        hashed_pw = generate_password_hash(pwd)
        # new_entry = User(username=user, server_ip=ip, password=hashed_pw)
        new_entry = User(username=user, email=email, password=hashed_pw)

        db.session.add(new_entry)
        db.session.commit()
        
        print(f"DB Update: New user '{user}' registered successfully.")
        return redirect(url_for('login_page'))

    return render_template('Signup.html') # You need a Signup.html for this

# 2. Login Route: Checking details against the database
@app.route('/login', methods=['GET', 'POST'])
def login_page():
    if request.method == 'POST':
        user_input = request.form.get('username')
        pass_input = request.form.get('password')
        ip_input = request.form.get('server_ip')

        # Search database for the username
        user_record = User.query.filter_by(username=user_input).first()

        # Verify password and user existence
        if user_record and check_password_hash(user_record.password, pass_input):
            print(f"Login Success: {user_input} is monitoring {ip_input}")
            return render_template('dashboard.html', username=user_input, ip=ip_input, metrics={})
        else:
            return "<h1>Invalid Credentials!</h1><p>Please check your username/password or Create an Account.</p>"

    return render_template('Login.html')

if __name__ == '__main__':
    app.run(debug=True)