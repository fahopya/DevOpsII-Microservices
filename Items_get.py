from flask import Flask, request, jsonify
import datetime

import Items_data as us

app = Flask(__name__)


@app.route('/item', methods=['GET'])
def item():
    _item = us.items_name()
    return jsonify(_item)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5005, debug=True) 