from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <html>
    <head>
        <title>0x App</title>
        <style>
            body { 
                font-family: Arial; 
                text-align: center; 
                margin: 50px;
                background: linear-gradient(135deg, #667eea, #764ba2);
                color: white;
            }
            .container {
                background: rgba(255,255,255,0.1);
                padding: 40px;
                border-radius: 20px;
                backdrop-filter: blur(10px);
                max-width: 600px;
                margin: 0 auto;
            }
            h1 { font-size: 2.5em; margin-bottom: 20px; }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>🔥 0x Application</h1>
            <p>Always Online • Cloud Hosted</p>
            <p>Powered by Python + Flask</p>
            <div style="margin-top: 30px;">
                <p><strong>Status:</strong> 🟢 Running</p>
                <p><strong>Host:</strong> Render.com</p>
                <p><strong>URL:</strong> Always Available</p>
            </div>
        </div>
    </body>
    </html>
    '''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
