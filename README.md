# jupyterlab-app-template

Kickstart your JupyterLab based application 🚀

This template:

- is heavily inspired by the [JupyterLab standalone examples](https://github.com/jupyterlab/jupyterlab/tree/master/examples)
- provides the basic structure to use a custom `JupyterFrontEnd.IShell`

## Usage

Create a new repo using this template:

Alternatively, clone the repo with the following command to retrieve the source:

```bash
git clone https://github.com/jtpio/jupyterlab-app-template
```

To set up the dev environment:

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
