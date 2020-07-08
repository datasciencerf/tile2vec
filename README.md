This code is modified from https://github.com/ermongroup/tile2vec
#### Prepare Descartes Lab workspace
* Start up GPU instance of Descartes Workbench
* Install compatible version of PyTorch and TorchVision:
    * Open a new terminal
        * run `pip install torch==1.5.1+cu101 torchvision==0.6.1+cu101 -f https://download.pytorch.org/whl/torch_stable.html`
    * OR place at top of notebook:
        * `!pip install torch==1.5.1+cu101 torchvision==0.6.1+cu101 -f https://download.pytorch.org/whl/torch_stable.html`
* See Notebook from Tile2Vec Authors below on example usage:
    * https://github.com/ermongroup/tile2vec/blob/master/examples/Example%202%20-%20Train%20Tile2Vec%20from%20scratch.ipynb