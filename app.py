from flask import Flask, render_template, send_file, request
from io import StringIO
import qrcode

app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html')

#def serve_pil_image(pil_img):
#    img_io = StringIO()
#    pil_img.save(img_io, 'JPEG', quality=70)
#    img_io.seek(0)
#    return send_file(img_io, mimetype='image/jpeg')

@app.route('/qr/<name>')
def qr(name):
    img = qrcode.make(name)
    img.save('test.jpg')
    return send_file('test.jpg', mimetype='image/jpeg')

@app.route('/qr_maker', methods=['GET', 'POST'])
def qr_maker():
    if request.method == 'POST' and request.form.get('qr_code'):
        return qr(request.form.get('qr_code'))
    return render_template('qr.html')
