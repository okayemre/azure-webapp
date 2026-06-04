from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>My Azure Web App</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
            background: linear-gradient(135deg, #2ea44f, #0078d4);
            color: white;
        }
        .container {
            text-align: center;
            padding: 40px;
            background: rgba(255,255,255,0.15);
            border-radius: 16px;
        }
        h1 { font-size: 2.5em; }
        p  { font-size: 1.2em; opacity: 0.9; }
    </style>
</head>
<body>
    <div class="container">
        <h1>Hello from GitHub!</h1>
        <p>Deployed automatically via CI/CD.</p>
        <p>It works! ✅</p>
    </div>
</body>
</html>
"""

if __name__ == '__main__':
    app.run()
