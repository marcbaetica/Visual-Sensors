from flask import Flask, request, jsonify


app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello world!'


@app.route('/post', methods=['POST'])
def test_post():
    input_json = request.get_json(force=True)
    response = {'text': input_json['text']}
    return jsonify(response)


app.run(port=5000)
# Alternatively:
# export FLASK_APP=hello.py
# flask run
