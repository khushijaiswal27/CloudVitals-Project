from flask import Flask, render_template  # <--- render_template ko yahan add karo

app = Flask(__name__)

@app.route('/')

def home():
    # Ab ye "index.html" ko templates folder mein dhundega
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)