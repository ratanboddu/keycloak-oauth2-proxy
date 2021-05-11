from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/app1')
def home():
    return 'Home Landing Page'

@app.route('/app1/api1/landing')
def api1():
    return 'API 1 : Landing Page'

@app.route('/app1/api2/landing')
def api2():
    return 'API 2 : Landing Page'

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5678)

