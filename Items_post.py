from flask import Flask, request, jsonify
import datetime
import Items_data as us

app = Flask(__name__)

@app.route('/items', methods=['POST'])
def createitems():
   
    name = request.form.get('name')
    category = request.form.get('category')
    price = request.form.get('price')
    instock = request.form.get('instock')

    _user = us.items_name()
    data = [x for x in _user if x["name"]==name]
    
    if (data):
        return jsonify({'message': 'Cannot create your items.'}), 401
    else:
        us.items_name_add(name,category,price,instock)
        return jsonify({'message': 'Create successfully.'}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002, debug=True) 