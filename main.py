from selenium import webdriver
from selenium.webdriver.common.by import By

from mongo import MongoConnection


db_client = MongoConnection().client
db = db_client.get_database('ebay')
col = db.get_collection('relojes')

driver = webdriver.Chrome()
driver.get("https://www.ebay.com/e/latam/luxurywatches?_trkparms=pageci%3Adccab2fb-5f2e-11ee-9e84-f6ec8a7d2116%7Cparentrq%3Ae3a7c31f18a0a56184d7cfe3fffe68ce%7Ciid%3A1")

flights = driver.find_elements(By.CLASS_NAME, "s-item__wrapper clearfix") #conunto de image,valores
for f in flights:
    nombre_articulo = f.find_element(by=By.CLASS_NAME, value="s-item__title").text
    precio = f.find_element(by=By.CLASS_NAME, value="s-item__trending-price").text
    precio_envio = f.find_element(by=By.CLASS_NAME, value="s-item__shipping s-item__logisticsCost").text

    #price = f.find_element(by=By.CLASS_NAME, value="price").text  #borrador de linea

    document = {
     #   "airline": airline_name,     #borrador de linea
        "nombre del artículo: ": nombre_articulo,
        "Precio: ": precio,
        "Valor de envío: ": precio_envio
      #  "price": price
    }

    col.insert_one(document=document)
    print("Nombre del artículo: ", nombre_articulo)
    print("Precio: ", precio)
    print("Valor de envio: ", precio_envio)
    #print(price)   #borrador de linea
    print('=' * 40)


driver.close()

