from pathlib import Path
from setuptools import setup

from jupyter_packaging import (
    create_cmdclass,
    install_npm,
    ensure_targets,
    combine_commands,
)


HERE = Path(__file__).parent

{{cookiecutter.python_package_name}}_DIR = HERE / "{{cookiecutter.python_package_name}}"

jstargets = [
    ({{cookiecutter.python_package_name}}_DIR / "static" / "bundle.js").resolve(),
]

cmdclass = create_cmdclass("jsbuild", package_data_spec={"{{cookiecutter.python_package_name}}": "**"})
cmdclass["jsbuild"] = combine_commands(
    install_npm(HERE.resolve(), npm=["jlpm"], build_cmd="build"), ensure_targets(jstargets),
)

setup(cmdclass=cmdclass)
