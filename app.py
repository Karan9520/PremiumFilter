from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_wprld():
    return 'GreyMatters'


if __name__ == "__main__":
    app.run()
