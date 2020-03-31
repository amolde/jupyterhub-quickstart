# oc delete all,configmap,pvc,serviceaccount,rolebinding --selector app=jupyterhub -n spark
# oc get oauthclient --selector app=jupyterhub -n spark
# oc delete oauthclient --selector app=jupyterhub -n spark

git checkout tags/3.4.0
oc apply -n spark -f https://raw.githubusercontent.com/amolde/jupyter-notebooks/develop/image-streams/s2i-minimal-notebook.json
oc apply -n spark -f ../image-streams/jupyterhub.json
oc apply -n spark -f custom.notebook.images.yaml
oc start-build jupyter-notebook-scipy -n spark
oc start-build jupyter-notebook-tensorflow -n spark
oc start-build jupyter-notebook-pyspark -n spark
oc apply -n spark -f ../templates/jupyterhub-workspace.json 

# oc delete configmap --selector app=jupyterhub -n spark
# oc delete oauthclient --selector app=jupyterhub -n spark

oc project spark
oc new-app -n spark \
  --template jupyterhub-workspace \
  -p SPAWNER_NAMESPACE=`oc project --short` \
  -p NOTEBOOK_MEMORY=2Gi \
  -p VOLUME_SIZE=1Gi \
  -p IDLE_TIMEOUT=3600 \
  -p CLUSTER_SUBDOMAIN=ep-test.northeastern.edu \
  -p JUPYTERHUB_CONFIG="`cat jupyterhub.customizations.py`" \
