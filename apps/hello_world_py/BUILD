load("//bzl:py.bzl", "isaac_py_app")

filegroup(
    name = "codelets",
    srcs = glob(["codelets/*"]),
)

filegroup(
    name = "utils",
    srcs = glob(["utils/*"]),
)

filegroup(
    name = "graphs",
    srcs = glob(["graphs/*"]),
)

isaac_py_app(
    name = "hello_world",
    srcs = [
        "main.py",
        ":codelets",
        ":utils",
    ],
    data = [
        ":graphs",
    ],
    main = "main.py",
    modules = [
        "@com_nvidia_isaac_sdk//packages/sight",
    ],
    deps = ["@com_nvidia_isaac_sdk//packages/pyalice"],
)
