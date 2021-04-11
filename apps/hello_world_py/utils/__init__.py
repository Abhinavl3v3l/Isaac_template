import argparse

from .patch import patch_capnp_paths
from .websight_config import configure_websight_root


def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--is-deploy",
        action="store_true",
        help="starts an application in deployment mode",
    )
    return parser.parse_args()
