from flask import Flask, render_template, request

app = Flask(__name__)

# Supported locales
SUPPORTED_LOCALES = ['en', 'fr']

# Default locale
DEFAULT_LOCALE = 'en'

# Function to get the locale from the request
def get_locale():
    # Get locale from query parameter
    locale = request.args.get('locale')
    if locale and locale in SUPPORTED_LOCALES:
        return locale
    # Resort to default locale if not provided or unsupported
    return DEFAULT_LOCALE

@app.route('/')
def index():
    # Get the locale
    locale = get_locale()
    # Render the template with the correct locale
    return render_template('4-index.html', locale=locale)

if __name__ == '__main__':
    app.run(debug=True)

