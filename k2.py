from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def home():
    now = datetime.now()
    formatted_time = now.strftime("%A, %d %B %Y | %I:%M:%S %p")
    
    return f"""
    <html>
        <head>
            <title>Date & Time App</title>
            <style>
                body {{
                    background-color: #0f172a;
                    color: white;
                    font-family: Arial;
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    height: 100vh;
                }}
                div {{
                    background: #1e293b;
                    padding: 30px;
                    border-radius: 10px;
                    font-size: 22px;
                }}
            </style>
        </head>
        <body>
            <div>
                <h2>Current Date & Time</h2>
                <p>{formatted_time}</p>
            </div>
        </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)
