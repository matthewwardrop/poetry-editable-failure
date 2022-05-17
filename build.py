from pybind11.setup_helpers import Pybind11Extension, build_ext


def build(setup_kwargs):
    setup_kwargs.update(
        {
            "ext_modules": [
                Pybind11Extension(
                    "editable_failure.cpp_module",
                    ["src/cpp_module.cpp"],
                    language="c++",
                )
            ],
            "cmd_class": {"build_ext": build_ext},
            "zip_safe": False,
        }
    )
