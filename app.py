from flask_socketio import SocketIO, send, emit
from flask import Flask, render_template

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

@app.route('/')
@app.route('/index.html')
def hello_world():
    return render_template("base.html")

@socketio.on('message')
def handle_message(message):
    print(message)
    emit('notification', message, broadcast=True)

@app.route('/invoice/', methods=['POST','GET'])
def invoice_paid():
    invoice = None
    print(invoice)
    # notify everybody that we have a new payment
    socketio.emit('notification', invoice)
    return "OK"

@app.route('/route/', methods=['POST','GET'])
def payment_routed():
    # do nothing
    return "OK"

if __name__ == '__main__':
    socketio.run(app, debug=True, host="0.0.0.0", port=8080)