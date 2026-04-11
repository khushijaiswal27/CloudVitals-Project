from flask import Flask, render_template # <--- render_template ko yahan add karo

app = Flask(__name__)

#ye tumhara homepage hai
@app.route('/')
def home():
    # Ab ye "homepage.html" ko templates folder mein dhundega
    return render_template('homepage.html')

# Ye mera login page ka rasta hai
@app.route('/login')
def login_page():
    # Ab ye "Login.html" ko templates folder mein dhundega
    return render_template('Login.html')

if __name__ == '__main__':
    app.run(debug=True)  