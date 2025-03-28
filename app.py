from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))  # Use the PORT assigned by Render
    app.run(host="0.0.0.0", port=port, debug=True)
