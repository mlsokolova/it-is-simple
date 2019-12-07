#!/bin/bash
export CONDA_DIR="$HOME/miniconda3"
export NOTEBOOK_DIR="$HOME/projects/it-is-simple/gis_jupyter/jupyter_notebooks"
export CONFIG_FILE="jupyter_notebook_config.py"
source $CONDA_DIR/etc/profile.d/conda.sh
conda activate jupyter_env
nohup $CONDA_DIR/envs/jupyter_env/bin/jupyter-notebook --config $CONFIG_FILE  --no-browser --notebook-dir=$NOTEBOOK_DIR 2>&1>jupyter_notebook.out &
