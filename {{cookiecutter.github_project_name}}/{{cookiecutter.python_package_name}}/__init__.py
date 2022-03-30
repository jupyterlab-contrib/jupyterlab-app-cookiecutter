"""
Copyright (c) Jupyter Development Team.
Distributed under the terms of the Modified BSD License.

Example
-------

To run the example, see the instructions in the README to build it. Then
run ``{{cookiecutter.python_package_name}}``.

"""
import os

from jupyter_server.base.handlers import JupyterHandler
from jupyter_server.extension.handler import (
    ExtensionHandlerMixin,
    ExtensionHandlerJinjaMixin
)
from jupyterlab_server import LabServerApp
from jupyter_server.utils import url_path_join as ujoin

from ._version import __version__

HERE = os.path.dirname(__file__)


def _jupyter_server_extension_points():
    return [
        {
            'module': __name__,
            'app': ExampleApp
        }
    ]


class ExampleHandler(
    ExtensionHandlerJinjaMixin,
    ExtensionHandlerMixin,
    JupyterHandler
        ):
    """Handle requests between the main app page and notebook server."""

    def get(self):
        """Get the main page for the application's interface."""
        config_data = {
            # Use camelCase here, since that's what the lab components expect
            "appVersion": __version__,
            'baseUrl': self.base_url,
            'token': self.settings['token'],
            'fullStaticUrl': ujoin(self.base_url, 'static', self.name),
            'frontendUrl': ujoin(self.base_url, 'example/'),
        }
        return self.write(
            self.render_template(
                'index.html',
                static=self.static_url,
                base_url=self.base_url,
                token=self.settings['token'],
                page_config=config_data
                )
            )


class ExampleApp(LabServerApp):

    extension_url = '/example'
    default_url = '/example'
    app_url = "/example"
    load_other_extensions = False
    name = __name__
    app_name = 'JupyterLab App Template'
    static_dir = os.path.join(HERE, 'static')
    templates_dir = os.path.join(HERE, 'templates')
    app_version = __version__
    app_settings_dir = os.path.join(HERE, 'static', 'application_settings')
    schemas_dir = os.path.join(HERE, 'static', 'schemas')
    themes_dir = os.path.join(HERE, 'static', 'themes')
    user_settings_dir = os.path.join(HERE, 'static', 'user_settings')
    workspaces_dir = os.path.join(HERE, 'static', 'workspaces')

    def initialize_handlers(self):
        """Add example handler to Lab Server's handler list.
        """
        super().initialize_handlers()
        self.handlers.append(('/example', ExampleHandler))


main = ExampleApp.launch_instance
