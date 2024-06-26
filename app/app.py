from flask import Flask, send_file
from plotdata import regression_plot

app = Flask(__name__)

@app.route('/', methods = ['GET'])
def regr_plot():
    image = regression_plot()

    return send_file(image,
    download_name='regplot.png',
    mimetype = 'image/png' )

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000, debug = False)

