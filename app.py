def app(environ, start_response):
    status = "200 OK"
    html = b"""
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
        <p>This code was deployed automatically.</p>
        <p>CI/CD is working! ✅</p>
    </div>
</body>
</html>
    """
    headers = [
        ("Content-Type", "text/html; charset=utf-8"),
        ("Content-Length", str(len(html)))
    ]
    start_response(status, headers)
    return [html]
