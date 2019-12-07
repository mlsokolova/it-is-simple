FROM centos:7
RUN useradd jupyter
RUN yum install -y python3 wget epel-release && yum install -y python3-pip
ENV LANG=en_US.UTF-8
ENV LANGUAGE=en_US.UTF-8
ADD ./ /opt/gis_jupyter/
RUN chown -R jupyter:jupyter /opt/gis_jupyter
WORKDIR /opt/gis_jupyter
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt
RUN jupyter nbextension enable --py --sys-prefix ipyleaflet
RUN jupyter nbextension     enable --py --sys-prefix appmode
RUN jupyter serverextension enable --py --sys-prefix appmode
USER jupyter:jupyter
RUN mkdir /opt/gis_jupyter/conf
ENV JUPYTER_CONFIG_DIR /opt/gis_jupyter/conf
RUN jupyter-notebook --generate-config
RUN echo -e "\nc.Appmode.show_edit_button = False\nc.Appmode.show_other_buttons = False" >> /opt/gis_jupyter/conf/jupyter_notebook_config.py
CMD jupyter-notebook --ip=0.0.0.0 --port=8888 --config "/opt/gis_jupyter/conf/jupyter_notebook_config.py" --no-browser --notebook-dir "/opt/gis_jupyter/jupyter_notebooks"
