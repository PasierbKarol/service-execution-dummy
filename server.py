from flask import Flask, abort, redirect, request

app = Flask(__name__)


@app.before_request
def log_request_info():
    app.logger.debug('Headers: %s', request.headers)
    app.logger.debug('Body: %s', request.get_data())


@app.route("/large", methods=['POST'])
def large_response():
    return "x"*1500000


@app.route('/moved', methods=['GET'])
def permanent_redirect():
    #301
    return redirect('/you_were_redirected', code=301, Response=None)


@app.route('/temporary', methods=['GET'])
def temporary_redirect():
    #302
    return redirect('/you_were_redirected', code=302, Response=None)


@app.route('/other', methods=['GET'])
def see_other():
    #303
    return redirect('/you_were_redirected', code=303, Response=None)


@app.route('/', methods=['GET'])
def index():
    return "{ \"message\":\"Main Page\"}"


@app.route('/404', methods=['GET'])
def not_found():
    abort(404)
    return "{ \"message\":\"NOT FOUND\"}"


@app.route("/you_were_redirected")
def redirected_message():
    return "You were redirected. Congrats :)!"
