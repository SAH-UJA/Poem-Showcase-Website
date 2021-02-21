from flask import *
import json
app = Flask(__name__)

@app.route('/')
def index():
    with open('data.json', 'rb') as f:
        d = json.loads(f.read())
        return render_template('index.html', data = d)