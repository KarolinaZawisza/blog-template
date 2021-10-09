from flask import Flask, render_template
import requests
app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template('index.html')

@app.route('/blog')
def blog():
    response = requests.get('https://api.npoint.io/49943cbdc8ee3ec5a615').json()
    return render_template('blog.html', title=response['title'], blog=response['blog'], link=response['link'])


if __name__ == '__main__':
    app.run(debug=True)
