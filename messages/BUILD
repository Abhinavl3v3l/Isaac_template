load("@com_nvidia_isaac_engine//bzl:isaac_engine.bzl", "isaac_cc_library")
load("//messages:messages.bzl", "create_message_proto_libraries", "message_proto_library_names")

filegroup(
    name = "capnp",
    srcs = glob(["*.capnp"]),
    visibility = ["//visibility:public"],
)

create_message_proto_libraries()

isaac_cc_library(
    name = "my_proto",
    hdrs = ["my_proto.hpp"],
    visibility = ["//visibility:public"],
    deps = [
        "@com_nvidia_isaac_sdk//messages:proto_registry",
        "my_proto_proto",
    ]
)
