from pulsar import Function

class RoutingFunction(Function):
    def __init__(self):
        f=open("functionlogs.txt","a")
        f.write("INIT        " + "\n")
        f.close()

        self.fruits_topic = "persistent://public/default/fruits"
        self.vegetables_topic = "persistent://public/default/vegetables"

    @staticmethod
    def is_fruit(item):
        f=open("functionlogs.txt","a")
        f.write("is_fruit        " + "\n")
        f.close()

        return item in ["apple", "orange","pear", "other fruits..."]

    @staticmethod
    def is_vegetable(item):
        f=open("functionlogs.txt","a")
        f.write("is_vegetable        " + "\n")
        f.close()

        return item in ["carrot", "lettuce", "radish", "other vegetables..."]

    def process(self, item, context):
        f=open("functionlogs.txt","a")
        f.write("=======process" + "\n")
        f.write(item + "\n")


        if self.is_fruit(item):
            f.write("fruit\n")

            context.publish(self.fruits_topic, item)
        elif self.is_vegetable(item):
            f.write("self.is_vegetable \n")

            context.publish(self.vegetables_topic, item)
        else:
            warning = "The item {0} is neither a fruit nor a vegetable".format(>
            context.get_logger().warn(warning)
        f=open("functionlogs.txt","a")
        f.write(warning + "\n")
        f.write(self.fruits_topic + "\n")
        f.write(self.fruits_topic + "\n")

        f.write(item)
        f.close()


