from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "<h1>CloudVitals Server is Running!</h1><p>Khushi, tumhara pehla backend successfully chal gaya!</p>"

if __name__ == '__main__':
    app.run(debug=True)