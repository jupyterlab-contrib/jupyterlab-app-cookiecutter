# jupyterlab-app-template

Kickstart your JupyterLab based application 🚀

This template:

- is heavily inspired by the [JupyterLab standalone examples](https://github.com/jupyterlab/jupyterlab/tree/master/examples)
- provides the basic structure to use a custom `JupyterFrontEnd.IShell`

![template-screencast](https://user-images.githubusercontent.com/591645/100390555-18a61380-3031-11eb-9ebc-ff81a5924b16.gif)

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
