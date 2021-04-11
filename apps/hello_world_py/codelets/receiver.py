from isaac import Codelet


class Receiver(Codelet):
    def start(self):
        self.input = self.isaac_proto_rx("MyCustomProto", "number")
        self.tick_on_message(self.input)

    def tick(self):
        print(self.input.message.proto.myValue)
