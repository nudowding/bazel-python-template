load("@rules_python//python:defs.bzl", "py_library")

py_library(
    name = "lib_py",
    srcs = glob(["**/*.py"]),
    imports = ["."],
    visibility = ["//:__subpackages__"],
)
