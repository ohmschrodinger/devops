from flask import Flask

app = Flask(__name__)

print("User authentication feature branch initialized. from main branch")

@app.route("/")
def home():
    return "Hello, World!"

if __name__ == "__main__":
    app.run(debug=True)