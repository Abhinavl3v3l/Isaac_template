from isaac import Codelet


class Sender(Codelet):
    def start(self):
        self.output = self.isaac_proto_tx("MyCustomProto", "number")
        self.tick_periodically(1)

    def tick(self):
        tx_builder = self.output.init()
        tx_builder.proto.myValue = self.config["number"] or 0

        self.output.publish()
