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
from flask import Flask, render_template, request  # 1. 'request' ko add kiya data lene ke liye

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('homepage.html')

# 2. 'methods' mein GET aur POST dono dale hain
@app.route('/login', methods=['GET', 'POST'])
def login_page():
    if request.method == 'POST':
        # 3. HTML ke 'name' attribute se data nikal rahe hain
        user = request.form.get('username')
        ip = request.form.get('server_ip')
        
        # 4. Ye tumhare VS Code ke Terminal mein dikhega
        print(f"\n--- Data Received from Frontend ---")
        print(f"Username: {user}")
        print(f"IP Address: {ip}")
        print(f"-----------------------------------\n")
        
        return f"<h1>Success!</h1><p>Khushi, humne '{user}' aur IP '{ip}' pakad liya hai. Terminal check karo!</p>"

    # Agar normal page khul raha hai (GET), toh sirf form dikhao
    return render_template('Login.html')

if __name__ == '__main__':
    app.run(debug=True)