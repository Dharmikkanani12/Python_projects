from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/projects')
def projects():
    projects = [
        {
            "name": "Weather Dashboard",
            "description": "A web app that fetches weather data and shows forecasts.",
            "url": "https://github.com/yourusername/weather-dashboard"
        },
        # Add more projects as needed
    ]
    return render_template('projects.html', projects=projects)

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)
