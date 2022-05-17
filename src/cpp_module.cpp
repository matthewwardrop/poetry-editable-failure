#include <pybind11/pybind11.h>
#include <pybind11/stl.h>

float add(float a, float b) {
    return a + b;
}

namespace py = pybind11;

PYBIND11_MODULE(cpp_module, m)
{
  m.doc() = "Example C++ module.";

  m.def("add", &add, "Add two numbers.");
}
