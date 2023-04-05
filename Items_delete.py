from flask import Flask, request, jsonify
import datetime
import Items_data as us

app = Flask(__name__)

@app.route('/delete', methods=['DELETE'])
def delete():
    name = request.form.get('name')
    _user = us.find_itemsname(name)
    data = [x for x in _user if x["name"]==name]
    if data:
        us.items_delete(name)
        return jsonify({'message': 'Delete successfully!'}), 200
    else:
        return jsonify({'message': 'Cannot delete your items!'}), 401

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5003, debug=True) 