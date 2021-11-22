import os
from flask import Flask, render_template
from flask import request
import qrcode
from IPython.display import Image

# print a nice greeting.
def say_hello(username = "World"):
    return '<p>Hello %s!</p>\n' % username

# EB looks for an 'application' callable by default.
application = Flask(__name__)

@application.route("/")
def hello():
 return "Hello World!"
 
@application.route("/index")
def index():
 return render_template('index.html')

@application.route("/generate", methods = ['POST'])
def generate():
    sText  = request.form['txtQRCODE']
    
    input_data = sText
    
    #Creating an instance of qrcode
    qr = qrcode.QRCode(
            version=1,
            box_size=10,
            border=5)
            
    qr.add_data(input_data)
    qr.make(fit=True)
    UPLOADS_PATH = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'static/images')

    img = qr.make_image(fill='black', back_color='white')
    img.save(os.path.join(UPLOADS_PATH, 'qrcode001.png'))

    #img.save('os.path.join(C:\\PauloMelo\\qrcode\\qrcode001.png')

    result = {
        'sText': sText
    }


    return render_template('index.html',result=result)


# run the app.
if __name__ == "__main__":
    # Setting debug to True enables debug output. This line should be
    # removed before deploying a production app.
    application.debug = True
    application.run()