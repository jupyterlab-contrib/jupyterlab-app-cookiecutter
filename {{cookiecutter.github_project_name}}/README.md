# {{cookiecutter.github_project_name}}

[![Github Actions Status](https://github.com/{{cookiecutter.github_organization_name}}/{{cookiecutter.github_project_name}}/workflows/Build/badge.svg)](https://github.com/{{cookiecutter.github_organization_name}}/{{cookiecutter.github_project_name}}/actions)

Your JupyterLab based application 🚀

This:

- is heavily inspired by the [JupyterLab standalone examples](https://github.com/jupyterlab/jupyterlab/tree/master/examples)
- provides the basic structure to use a custom `JupyterFrontEnd.IShell`

![template-screencast](https://user-images.githubusercontent.com/591645/100391887-307f9680-3035-11eb-97ee-c368b14c5f00.gif)

## Installation

Create a conda environment with the right dependencies then install with pip:

```bash
# Create a new environment
mamba create -n {{cookiecutter.github_project_name}} -c conda-forge nodejs yarn python jupyterlab_server=2 -y
conda activate {{cookiecutter.github_project_name}}

# Install the app
pip install -e .

# Run the app
{{cookiecutter.github_project_name}}
```

There is a watch command to automatically rebuild the application when there are new changes on the TypeScript code (you'll need to refresh the browser page):

```bash
yarn run watch
```

## Adding new plugins

One of the main benefits of building a JupyterLab-based application is that it makes it easier to reuse existing plugins and extensions that have been developed for JupyterLab.

Since this template uses the same plugin system as the one used in JupyterLab, and exposes a `JupyterFrontEnd.IShell` as the application shell, reusing other components becomes seamless.

### Add the dependency

The first step is to add the dependency to the `package.json`. Here using the [jupyterlab-plugin-graph](https://github.com/jupyterlab-contrib/jupyterlab-plugin-graph) JupyterLab extension available on npm:

```diff
--- a/package.json
+++ b/package.json
@@ -36,6 +36,7 @@
     "@jupyterlab/theme-light-extension": "^3.0.0-rc.10",
     "@jupyterlab/ui-components": "^3.0.0-rc.10",
     "@lumino/widgets": "^1.14.0",
+    "jupyterlab-plugin-graph": "^0.2.0",
     "es6-promise": "~4.2.8"
   },
   "devDependencies": {
```

Run `yarn` to install the dependency.

### Load the plugin

To load the plugin on startup, add it to the list of mods in `index.ts`:

```diff
--- a/src/index.ts
+++ b/src/index.ts
@@ -19,7 +19,8 @@ async function main(): Promise<void> {
   const mods = [
     require('./plugins/paths'),
     require('./plugins/top'),
-    require('./plugins/example')
+    require('./plugins/example'),
+    require('jupyterlab-plugin-graph')
   ];

   app.registerPluginModules(mods);
```

Since this plugin exposes the `jupyterlab-plugin-graph:open` command, we can for example add it to the menu:

```diff
--- a/src/plugins/example/index.ts
+++ b/src/plugins/example/index.ts
@@ -60,7 +60,10 @@ const plugin: JupyterFrontEndPlugin<void> = {
     });

     if (menu) {
-      menu.helpMenu.addGroup([{ command: CommandIDs.open }]);
+      menu.helpMenu.addGroup([
+        { command: CommandIDs.open },
+        { command: 'jupyterlab-plugin-graph:open' }
+      ]);
     }
   }
 };
```

### Rebuild and reload

Finally, rebuild the app with:

```bash
yarn run build
```

And reload the page to see the changes:

![new-plugin](https://user-images.githubusercontent.com/591645/100454221-c4487580-30bc-11eb-8c71-70988e36a686.gif)

### Custom plugins

Additionally, you can also add more custom plugins by following the pattern used for the [example plugin](https://github.com/{{cookiecutter.github_organization_name}}/{{cookiecutter.github_project_name}}/blob/main/src/plugins/example/index.ts).
