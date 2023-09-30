#import requests
from flask import Flask
from flask import render_template
from dotenv import load_dotenv
from mongo import MongoConnection

load_dotenv()

app = Flask(__name__)

db_client = MongoConnection().client
db = db_client.get_database('ebay')
col = db.get_collection('relojes')
@app.route('/')
def tabla_productos():
    products_data = col.find({})
    return render_template('tabla_productos.html', products=products_data)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=3501, debug=True)
