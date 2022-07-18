from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for, send_from_directory
from flask_pymongo import PyMongo
import certifi
app = Flask(__name__)


# mongodb_client = PyMongo(app, uri="mongodb+srv://admin:Welcome12@cluster0.bl8vv.mongodb.net/SampleDB?retryWrites=true&w=majority")
# db = mongodb_client.db

app.config["MONGO_URI"] = "mongodb+srv://admin:Welcome12@cluster0.bl8vv.mongodb.net/SampleDB?retryWrites=true&w=majority"
mongodb_client = PyMongo(app)
db = mongodb_client.db

@app.route('/')
def index():
   print('Request for index page received')
   return render_template('index.html')

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route('/hello', methods=['POST'])
def hello():
   name = request.form.get('name')
   db.User.insert_one({'name':name,'email': f'{name}@example.com'})
   if name:
       print('Request for hello page received with name=%s' % name)
       return render_template('hello.html', name = name)
   else:
       print('Request for hello page received with no name or blank name -- redirecting')
       return redirect(url_for('index'))


if __name__ == '__main__':
   app.run()