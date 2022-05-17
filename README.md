# Example project demonstrating failure of poetry to correctly install packages with compiled dependencies.


When you have configured poetry to generate a setup file, for example by using:

```
[tool.poetry.build]
script = "build.py"
generate-setup-file = true
```

and then attempt an editable install, poetry will include the module in the
generated wheel, which leads to it being added to the `site-packages` folder,
breaking the whole point of the editable installation. Moreover, compiled
modules are not built in-place, meaning that the module cannot be used
"editably" even if that issue were resolved.

See [poetry-core#335](https://github.com/python-poetry/poetry-core/pull/335) for
more details, and a potential fix.

## Reproduction

To reproduce the issue, run `pip install -e .` in the root folder of a checked
out copy of this repository. You will note:

1. `editable_failure` is installed into the site-packages folder of the
    appropriate Python installation. (PEP 660 indicates that only the files
    necessary to create an editable installation should be included; see
    https://peps.python.org/pep-0660/#what-to-put-in-the-wheel ).
2. `cpp_module` is not built inplace in the local checked out copy of the
    module, which is necessary if you actually wanted to use the Python code
    in an editable manner. (This is an optional feature suggested by PEP 660;
    see https://peps.python.org/pep-0660/#build-editable).

If you comment out the `poetry-core` build requirement in the `pyproject.toml` file,
uncomment the `"poetry-core @ git+https://github.com/matthewwardrop/poetry-core.git@fix_editable_installs"`
requirement, and then rerun `pip install -e .`, things work as they should.

## Other notes

Using `poetry` instead of `poetry-core` does not fix anything.

