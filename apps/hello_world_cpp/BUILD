load("@com_nvidia_isaac_sdk//bzl:module.bzl", "isaac_app", "isaac_cc_module")

isaac_cc_module(
    name = "sender",
    srcs = ["sender.cpp"],
    hdrs = ["sender.hpp"],
    deps = [
        "//messages:my_proto"
    ]
)

isaac_cc_module(
    name = "receiver",
    srcs = ["receiver.cpp"],
    hdrs = ["receiver.hpp"],
    deps = [
        "//messages:my_proto"
    ]
)

isaac_app(
    name = "hello_world",
    app_json_file = "graphs/hello_world.app.json",
    modules = [
        "//apps/hello_world_cpp:sender",
        "//apps/hello_world_cpp:receiver",
        "@com_nvidia_isaac_sdk//packages/sight"
    ]
)
