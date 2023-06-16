from flask import Flask, request, jsonify

from main import chatwithbot

app = Flask(__name__)


@app.route('/chat', methods=['GET', 'POST'])
def chatBot():
    chatInput = request.form['chatInput']
    return jsonify(chatBotReply=chatwithbot(chatInput))


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000)