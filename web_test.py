from flask import Flask, render_template_string, jsonify
from car_rental_app.localization.translations import translator, t

app = Flask(__name__)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Car Rental App Test Interface</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 40px;
            line-height: 1.6;
            background-color: #f5f5f5;
        }
        .container {
            max-width: 800px;
            margin: 0 auto;
        }
        .card {
            background-color: white;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            margin-bottom: 20px;
        }
        .language-selector {
            margin-bottom: 20px;
        }
        select {
            padding: 8px;
            border-radius: 4px;
            border: 1px solid #ddd;
        }
        .translation-test {
            background-color: #e8f5e9;
            padding: 15px;
            border-radius: 4px;
            margin-top: 10px;
        }
    </style>
    <script>
        function changeLanguage() {
            const lang = document.getElementById('language').value;
            fetch(`/change-language/${lang}`)
                .then(response => response.json())
                .then(data => {
                    document.getElementById('app-title').textContent = data.app_title;
                    document.getElementById('login-title').textContent = data.login_title;
                    document.getElementById('email-label').textContent = data.email_label;
                });
        }
    </script>
</head>
<body>
    <div class="container">
        <div class="card">
            <h1>Car Rental App Test Interface</h1>
            <div class="language-selector">
                <label for="language">Select Language:</label>
                <select id="language" onchange="changeLanguage()">
                    <option value="en">English</option>
                    <option value="fr">Français</option>
                    <option value="ar">العربية</option>
                </select>
            </div>
            <div class="translation-test">
                <h3>Translation Test</h3>
                <p>App Title: <span id="app-title">{{ app_title }}</span></p>
                <p>Login Title: <span id="login-title">{{ login_title }}</span></p>
                <p>Email Label: <span id="email-label">{{ email_label }}</span></p>
            </div>
        </div>
    </div>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(
        HTML_TEMPLATE,
        app_title=t("app.title"),
        login_title=t("login.title"),
        email_label=t("login.email_label")
    )

@app.route('/change-language/<lang>')
def change_language(lang):
    translator.set_language(lang)
    return jsonify({
        'app_title': t("app.title"),
        'login_title': t("login.title"),
        'email_label': t("login.email_label")
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000, debug=True)
