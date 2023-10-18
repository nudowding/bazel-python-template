load("@rules_python//python:defs.bzl", "py_test")
load("@pip_deps//:requirements.bzl", "requirement")

py_test(
    name = "test_package1",
    srcs = ["test_package1.py"],
    deps = [
        requirement("ward"),
        "//lib/package1:lib_py",
    ],
)
