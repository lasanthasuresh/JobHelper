from bottle import Bottle, template, static_file

app = Bottle()

@app.route('/')
def index():
    message = 'Hello, World!'
    return template('hello', message=message, title='Bottle Bootstrap Example')

@app.route('/static/<filename:path>')
def static(filename):
    return static_file(filename, root='static')

if __name__ == '__main__':
    app.run(host='localhost', port=8000, debug=True)
