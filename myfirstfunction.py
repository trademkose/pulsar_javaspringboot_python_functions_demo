from pulsar import Function
import json
from random import random
class MyFirstFunction(Function):
    def __init__(self):
        f=open("functionlogs.txt","w")
        f.write("MyFirstFunction started!" + "\n")
        f.close()
        self.current_tl_usd_currency=14.5
        self.smartphone_topic = "persistent://public/default/smartphone"
        self.computer_topic = "persistent://public/default/computer"

    def process(self, item, context):
        f=open("functionlogs.txt","a")
        f.write("INPUT ITEM" + "\n")
        f.write(item + "\n")
        data = json.loads(item)
        price_usd = data["price_usd"]
        price_tl = int(price_usd)*self.current_tl_usd_currency
        data["price_tl"] = price_tl
        if data["category_name"]=="smartphone":
                data["imei"] = int(random()*10000)
                f.write("INPUT is smartphone" + "\n")

                context.publish(self.smartphone_topic, json.dumps(data))
        elif data["category_name"]=="computer" :
                data["mac_adress"] = int(random()*100000000)
                f.write("INPUT is computer" + "\n")
                context.publish(self.computer_topic, json.dumps(data))
        else:
                warning = "The item {0} is neither a smartphone nor a computer".format(item)
                context.get_logger().warn(warning)
                f.write(warning + "\n")
        f.write("OUTPUT ITEM" + "\n")
        f.write(json.dumps(data) + "\n")
        f.close()
