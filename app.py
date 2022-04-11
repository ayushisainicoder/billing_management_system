from __future__ import division, print_function
import os
from flask import Flask, render_template, request
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = "uploaded_images"

for f in os.listdir("D:\\ayushi\\uploaded_images"):
    try:
        os.remove("D:\\ayushi\\uploaded_images" + f)
    except OSError:
        pass

# print('Model loaded. Check http://127.0.0.1:5000/')


@app.route('/', methods=['GET'])
def index():
    # Main page
    return render_template('upload.html')


@app.route('/uploader', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        # Get the file from post request
        f = request.files['file']

        # Save the file to ./uploads
        basepath = os.path.dirname(__file__)
        file_path = os.path.join(
            basepath, 'uploaded_images', secure_filename(f.filename))
        f.save(file_path)
        return "file uploaded successfully"


if __name__ == '__main__':
    app.run(debug=True)
    app.run('0.0.0.0', port=5001)
