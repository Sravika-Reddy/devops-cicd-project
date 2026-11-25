
from flask import Flask

# Create Flask application
app = Flask(__name__)

# Define the home page
@app.route("/")
def home():
    return "Welcome to our DevOps CI/CD Project!"

# Run the application
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
