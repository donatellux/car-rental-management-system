from flask import Flask, render_template_string
import threading
import flet as ft
import logging

app = Flask(__name__)

# Basic HTML template that will show our app is running
HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Car Rental App Status</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 40px;
            line-height: 1.6;
        }
        .status {
            padding: 20px;
            background-color: #f0f0f0;
            border-radius: 5px;
            margin-bottom: 20px;
        }
        .instructions {
            background-color: #e8f5e9;
            padding: 20px;
            border-radius: 5px;
        }
    </style>
</head>
<body>
    <div class="status">
        <h2>Car Rental Application Status</h2>
        <p>The Flet application is running.</p>
    </div>
    <div class="instructions">
        <h3>Test Credentials:</h3>
        <p>Email: admin@example.com</p>
        <p>Password: admin</p>
    </div>
</body>
</html>
"""

def run_flet_app():
    """Run the Flet application"""
    from car_rental_app.main import main
    try:
        # Try to run Flet app without specifying view mode
        ft.app(
            target=main,
            assets_dir="car_rental_app",
            port=5000  # Use a different port for Flet
        )
    except Exception as e:
        logging.error(f"Error starting Flet app: {e}")

@app.route('/')
def home():
    return render_template_string(HTML_TEMPLATE)

if __name__ == '__main__':
    # Start Flet app in a separate thread
    flet_thread = threading.Thread(target=run_flet_app)
    flet_thread.daemon = True
    flet_thread.start()
    
    # Run Flask app on port 3000
    app.run(host='0.0.0.0', port=3000)
