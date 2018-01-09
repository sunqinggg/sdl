from flask import Flask, render_template,request
from wtforms import Form, StringField, TextAreaField, RadioField, SelectField
app = Flask(__name__)


@app.route('/search')
def search():
    return render_template('search.html')




if __name__ == '__main__':
    app.run()
