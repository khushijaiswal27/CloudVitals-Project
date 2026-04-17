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
    print(f"Request Method: {request.method}")
    if request.method == 'POST':
        # 3. HTML ke 'name' attribute se data nikal rahe hain
        user = request.form.get('username')
        ip = request.form.get('server_ip') 
        
        # 4. Ye tumhare VS Code ke Terminal mein dikhega
        # print(f"\n--- Data Received from Frontend ---")
        # print(f"Username: {user}")
        # print(f"IP Address: {ip}")
        # print(f"-----------------------------------\n")

        # Terminal mein check krne k liye print kro
        print(f"User {user} is logging in for server: {ip}")

        # Yaha 'dashboard.html' ko link kar rhe hain
        # Hum 'username' aur 'ip' ko variable ke roop mein bhej rhe hai
        return render_template('dashboard.html', username=user, ip=ip)
        
        # return f"<h1>Success!</h1><p>'{user}' aur IP '{ip}'!</p>"

    # Agar user sirf page visit kar raha hai (GET), toh login form dikhao 
    return render_template('Login.html')

if __name__ == '__main__':
    app.run(debug=True)  