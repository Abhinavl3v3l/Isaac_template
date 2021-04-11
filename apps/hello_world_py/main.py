from apps.hello_world_py.utils import get_arguments
from isaac import Application

from codelets import Sender, Receiver
from utils import configure_websight_root, patch_capnp_paths, get_arguments


def main():
    # getting command line arguments
    args = get_arguments()

    # patching capnp paths. Needed if using isaac python API.
    patch_capnp_paths(args.is_deploy)

    # creating app
    app = Application(app_filename="apps/hello_world_py/graphs/graph.app.json")

    # adding python codelets to graph
    app.nodes["sender"].add(Sender, "sender_component")
    app.nodes["receiver"].add(Receiver, "receiver_component")

    # configuring Websight webroot and assetroot. Needed if using isaac python API.
    configure_websight_root(app)

    # running the application
    app.run()


if __name__ == "__main__":
    main()
