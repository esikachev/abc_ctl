from flask import Flask
from flask import request


abc_server = Flask(__name__)
abc_server.url_map.strict_slashes = False

from abc_server.flask import routes