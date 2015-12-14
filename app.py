from flask import Flask
from flask import Response
from flask import request
from flask.ext.cors import CORS
from werkzeug.http import HTTP_STATUS_CODES
from werkzeug.routing import BaseConverter

app = Flask(__name__)
app.debug = True
CORS(app)


class RegexConverter(BaseConverter):
  def __init__(self, url_map, *items):
    super(RegexConverter, self).__init__(url_map)
    self.regex = items[0]


app.url_map.converters['regex'] = RegexConverter


def response_body(mimetype):
  if mimetype.endswith('html'):
    return ''
  if mimetype.endswith('json'):
    return '{}'


def create_handler(path, code):
  def f(*args, **kwargs):
    mimetype = request.accept_mimetypes\
      .best_match(['application/json', 'text/html'])
    response = Response(response_body(mimetype),
                        status=code, mimetype=mimetype)
    return response
  return f


for code, msg in HTTP_STATUS_CODES.iteritems():
  path = '/%s<regex(".+"):path>' % (code)

  app.add_url_rule(path, msg, create_handler(path, code),
                   methods=['GET', 'POST', 'PUT', 'DELETE'])


if __name__ == "__main__":
  app.run(port=8888, host='0.0.0.0', use_debugger=True, debug=True,
      use_reloader=True)
