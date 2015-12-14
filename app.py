from flask import Flask
from flask import Response
from flask import request
from flask.ext.cors import CORS
from werkzeug.http import HTTP_STATUS_CODES

app = Flask(__name__)
app.debug = True
CORS(app)


def response_body(mimetype):
  if mimetype.endswith('html'):
    return ''
  if mimetype.endswith('json'):
    return '{}'


def create_handler(path, code):
  def f():
    mimetype = request.accept_mimetypes\
      .best_match(['application/json', 'text/html'])
    response = Response(response_body(mimetype),
                        status=code, mimetype=mimetype)
    return response
  return f


for code, msg in HTTP_STATUS_CODES.iteritems():
  path = "/%s" % (code)

  app.add_url_rule(path, msg, create_handler(path, code),
                   methods=['GET', 'POST', 'PUT', 'DELETE'])


if __name__ == "__main__":
  app.run(port=8888, host='0.0.0.0', use_debugger=True, debug=True,
      use_reloader=True)
