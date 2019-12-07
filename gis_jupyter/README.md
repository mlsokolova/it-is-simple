**GIS in Jupyter Notebook**  
_Goals:_  
1)Interact with the GIS in Jupyter Notebook. Mark 500 brownfield places on the map.  
2)Making web apps with Jupyter notebook.  

_Build and run:_  
```
docker build -m 1G --ulimit nofile=65536:65536 -t gis_jupyter .  
docker run --rm -p 8888:8888 gis_jupyter  
```
Output should be like this:  
```
    To access the notebook, open this file in a browser:
        file:///home/jupyter/.local/share/jupyter/runtime/nbserver-1-open.html
    Or copy and paste one of these URLs:
        http://ac06e42dcc13:8888/?token=404ada90034dded848110bb2f1ab426e5e3c5c23a26779c3
     or http://127.0.0.1:8888/?token=404ada90034dded848110bb2f1ab426e5e3c5c23a26779c3
```
Note:  
Copy token from the output (404ada90034dded848110bb2f1ab426e5e3c5c23a26779c3)  

_App link:_  
http://localhost:8888/apps/500_browfields.ipynb  
Note: Insert token into "password" field  

_Refs:_  
https://wiki.openstreetmap.org/wiki/Key:landuse  
https://wiki.openstreetmap.org/wiki/Sophox  
https://blog.jupyter.org/interactive-gis-in-jupyter-with-ipyleaflet-52f9657fa7a  
https://github.com/oschuett/appmode  
https://hackernoon.com/making-web-apps-with-jupyter-notebook-75eab8bdb092  

