from pulsar import Function
import json
from random import random
current_tl_usd_currency=14.5
class RoutingFunction(Function):
    def __init__(self):

        self.smartphone_topic = "persistent://public/default/smartphone"
        self.computer_topic = "persistent://public/default/computer"

    def process(self, item, context):
        f=open("functionlogs.txt","a")
        f.write("ITEM" + "\n")
        f.write(item + "\n")
        
        data = json.loads(item)
        price_usd=data["price_usd"]
        price_tl = int(price_usd)*current_tl_usd_currency
        data["price_tl"]= price_tl    
        if data["category_name"]=="smartphone":
            data["imei"] = int(random()*10000)
            context.publish(self.smartphone_topic, data)
        elif data["category_name"]=="computer" :
            data["mac_adress"] = int(random()*100000000)
            context.publish(self.computer_topic, data)             
        else:
            warning = "The item {0} is neither a fruit nor a vegetable".format(>
            context.get_logger().warn(warning)
        f.write(warning + "\n")
        f.write(data)
        f.close()


