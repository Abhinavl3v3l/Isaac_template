from isaac import CapnpMessages
from isaac import CodeletHooks
from isaac import Message


def patch_capnp_paths(is_deploy):
    if not is_deploy:
        isaac_messages = "/../com_nvidia_isaac_sdk/messages/*.capnp"
    else:
        isaac_messages = "/external/messages/*.capnp"
    custom_messages = "/messages/*.capnp"

    capnp_dict = {
        **_get_capnp_proto_schemata(custom_messages),
        **_get_capnp_proto_schemata(isaac_messages),
    }

    capnp_type_id_dict = {
        **_get_capnp_schema_type_id_dict(custom_messages),
        **_get_capnp_schema_type_id_dict(isaac_messages),
    }

    CodeletHooks.CAPNP_DICT = capnp_dict
    Message.CAPNP_DICT = capnp_dict
    Message.CAPNP_TYPE_ID_DICT = capnp_type_id_dict


def _get_capnp_proto_schemata(path):
    CapnpMessages.PATH = path
    return CapnpMessages.get_capnp_proto_schemata()


def _get_capnp_schema_type_id_dict(path):
    CapnpMessages.PATH = path
    return CapnpMessages.capnp_schema_type_id_dict()
