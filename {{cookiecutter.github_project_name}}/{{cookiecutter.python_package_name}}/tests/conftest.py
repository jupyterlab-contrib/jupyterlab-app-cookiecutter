import pytest
from {{cookiecutter.python_package_name}} import ExampleApp


@pytest.fixture
def base_url():
    return "/"


@pytest.fixture
def example_app(jp_serverapp):
    app = ExampleApp(open_browser=False)
    app._link_jupyter_server_extension(jp_serverapp)
    app.initialize()
    return app
