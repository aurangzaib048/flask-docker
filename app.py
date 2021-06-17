import structlog
from flask import Flask
import pathlib

app = Flask(__name__)

logger = structlog.getLogger(__name__)


@app.route('/')
def index():
    logger.info('<h1>Hello World!</h1><p> Please work!</p>')
    return '<h1>Hello World!</h1><p> Please work!</p>'


@app.route('/user/<name>')
def user(name):
    logger.info('<h1>Hello, {}!</h1>'.format(name))
    return '<h1>Hello, {}!</h1>'.format(name)

@app.route('/read')
def read_from_vol():
    dirpath = pathlib.Path("/data")
    logger.info("reading vol file")
    for x in dirpath.iterdir():
        if x.is_file():
            with x.open() as f:
                logger.info(f"Filename {x.name}")
                # file_data = f.read()
                logger.info('<h1>Read endpoint</h1>')

                return '<h1>{}</h1>'.format(f.read())


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
