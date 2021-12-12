from flask import *

app=Flask(__name__)

@app.route('/')
def home ():
    return render_template('index.html')

@app.route('/uma')
def uma_hello_world():
   return 'UMA Flask learning'

@app.route('/oviya')
def oviya_hello_world():
   return  'Oviya Flask learning'

if __name__ == '__main__':
   app.run(debug=True)
