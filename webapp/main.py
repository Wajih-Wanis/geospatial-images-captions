from flask import Flask, render_template, request, redirect, url_for
import os
from model import Model
from config import Config


app = Flask(__name__)
app.config.from_object(Config)

UPLOAD_FOLDER = app.config['UPLOAD_FOLDER']
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
LLM = Model(16,4)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/')
def index():
    return render_template('index.html', filename=None, caption=None)


@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return redirect(request.url)    

    file = request.files['file']

    if file.filename == '':
        return redirect(request.url)

    if file and allowed_file(file.filename):
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(file_path)
        
        
        caption = LLM.predict_step([file_path])

        return render_template('index.html', filename=file_path, caption=caption)

    return redirect(request.url)


if __name__ == '__main__':
    app.run(debug=True)
