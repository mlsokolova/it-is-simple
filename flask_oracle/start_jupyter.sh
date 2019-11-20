#!/bin/bash
export CONDA_DIR="/home/masha/miniconda3"
export NOTEBOOK_DIR="/home/masha"
source $CONDA_DIR/etc/profile.d/conda.sh
conda activate jupyter_env
export ORACLE_HOME="/home/masha/Downloads/instantclient_19_3"
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$ORACLE_HOME
nohup $CONDA_DIR/envs/jupyter_env/bin/jupyter-notebook --no-browser --notebook-dir=$NOTEBOOK_DIR 1>jupyter_notebook.out 2>jupyter_notebook.err &
