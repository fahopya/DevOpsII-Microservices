import sqlite3
import os

db_folder = os.path.join(os.path.dirname(__file__), "Items.db")

def items_name():
    data = []
    conn = sqlite3.connect(db_folder)
    sql = """
        SELECT name, category , price, instock
        FROM items
        ORDER BY name
    """
    cursor = conn.execute(sql)
    rows = cursor.fetchall()

    for row in rows:
        record = {
            'name': row[0],
            'category': row[1],
            'price': row[2],
            'instock':row[3]
            }
        data.append(record)
    
    conn.close()
    return data

def find_itemsname(items):
    data = []
    conn = sqlite3.connect(db_folder)
    sql = """
        SELECT name, category , price, instock
        FROM items
        WHERE name=?
    """
    val = (items,)
    cursor = conn.execute(sql,val)
    rows = cursor.fetchone()

    record = {
        'name': rows[0],
        'category': rows[1],
        'price': rows[2],
        'instock':rows[3]
        }
    data.append(record)
    
    conn.close()
    return data

def items_name_add(name,category,price,instock):
    conn = sqlite3.connect(db_folder)
    sql = """
        INSERT INTO items(name,category,price,instock)
        VALUES(?,?,?,?)
    """
    val = (name,category,price,instock)
    cursor = conn.execute(sql, val)
    conn.commit()
    conn.close()
    return "Create successfully!"

def items_delete(items):
    conn = sqlite3.connect(db_folder)
    sql = """
        DELETE FROM item
        WHERE name=?
    """
    val = (items,)
    cursor = conn.execute(sql, val)
    conn.commit()
    conn.close()
    return "Delete successfully!"

def update_items(name,category,price,instock):
    conn = sqlite3.connect(db_folder)
    sql = """
        UPDATE items
        SET category=? , price=?, instock=?
        WHERE name=?
    """
    val = (category,price,instock,name)
    cursor = conn.execute(sql, val)
    conn.commit()
    conn.close()
    return "Update successfully!"