from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def home():
    now = datetime.now()
    formatted_time = now.strftime("%A, %d %B %Y | %I:%M:%S %p")
    return render_template("index.html", current_time=formatted_time)

if __name__ == "__main__":
    app.run(debug=True)
