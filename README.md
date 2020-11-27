# jupyterlab-app-template

[![Github Actions Status](https://github.com/jtpio/jupyterlab-app-template/workflows/Build/badge.svg)](https://github.com/jtpio/jupyterlab-app-template/actions)

Kickstart your JupyterLab based application 🚀

This template:

- is heavily inspired by the [JupyterLab standalone examples](https://github.com/jupyterlab/jupyterlab/tree/master/examples)
- provides the basic structure to use a custom `JupyterFrontEnd.IShell`

![template-screencast](https://user-images.githubusercontent.com/591645/100391887-307f9680-3035-11eb-97ee-c368b14c5f00.gif)

## Usage

Create a new repo using this template:

![image](https://user-images.githubusercontent.com/591645/100390502-e2689400-3030-11eb-8558-c450d7976858.png)

Alternatively, clone the repo with the following command to retrieve the source:

```bash
git clone https://github.com/jtpio/jupyterlab-app-template
cd jupyterlab-app-template/
```

Then:

```bash
# create a new environment
mamba create -n jupyterlab-app-template -c conda-forge/label/jupyterlab_server_rc -c conda-forge nodejs yarn python jupyterlab_server=2 -y
conda activate jupyterlab-app-template

# install the dependencies
yarn

# build the app
yarn run build

# run the app
python main.py
```

There is also a watch command to automatically rebuild the application when there are new changes:

```bash
yarn run watch
```

## Adding new plugins

One of the main benefits of building a JupyterLab-based application is that it makes it easier to reuse existing plugins and extensions that have been developed for JupyterLab.

Since this template uses the same plugin system as the one used in JupyterLab, and exposes a `JupyterFrontEnd.IShell` as the application shell, reusing other components becomes seamless.

### Add the dependency

The first step is to add the dependency to the `package.json`. Here using the [jupyterlab-plugin-graph](https://github.com/jtpio/jupyterlab-plugin-graph) JupyterLab extension available on npm:

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

Additionally, you can also add more custom plugins by following the pattern used for the [example plugin](https://github.com/jtpio/jupyterlab-app-template/blob/main/src/plugins/example/index.ts).

## Contributing

If you think there should be other defaults as part of this template, please open a new [issue](https://github.com/jtpio/jupyterlab-app-template/issues) or [pull request](https://github.com/jtpio/jupyterlab-app-template/pulls)!
