c.Authenticator.admin_users = {'a.deshmukh'}
c.Authenticator.whitelist = {'kafka.admin'}

c.KubeSpawner.profile_list = [
    {
        'display_name': 'Minimal Notebook - Classic (Python 3.5)',
        'kubespawner_override': {
            'image_spec': 'docker-registry.default.svc:5000/spark/s2i-minimal-notebook:3.5'
        }
    },
    {
        'display_name': 'Minimal Notebook - JupyterLab (Python 3.6)',
        'kubespawner_override': {
            'image_spec': 'docker-registry.default.svc:5000/spark/s2i-minimal-notebook:3.6',
            'environment': { 'JUPYTER_ENABLE_LAB': 'true' }
        }
    },
    {
        'display_name': 'Minimal Notebook - JupyterLab (Python 3.6)',
        'kubespawner_override': {
            'image_spec': 'docker-registry.default.svc:5000/spark/s2i-minimal-notebook:3.5',
            'environment': { 'JUPYTER_ENABLE_LAB': 'true' }
        }
    },
    {
        'display_name': 'Minimal Notebook (Python 3.6)',
        'default': True,
        'kubespawner_override': {
            'image_spec': 'docker-registry.default.svc:5000/spark/s2i-minimal-notebook:3.6'
        }
    },
    {
        'display_name': 'Tensorflow Notebook (Python 3.6)',
        'kubespawner_override': {
            'image_spec': 'docker-registry.default.svc:5000/spark/jupyter-notebook-tensorflow:latest'
        }
    },
    {
        'display_name': 'PySpark Notebook (Python 3.6)',
        'kubespawner_override': {
            'image_spec': 'docker-registry.default.svc:5000/spark/jupyter-notebook-pyspark:latest'
        }
    },
    {
        'display_name': 'Scipy Notebook (Python 3.6)',
        'kubespawner_override': {
            'image_spec': 'docker-registry.default.svc:5000/spark/jupyter-notebook-scipy:latest'
        }
    }
]

c.KubeSpawner.storage_pvc_ensure = True
c.KubeSpawner.pvc_name_template = c.KubeSpawner.pod_name_template
c.KubeSpawner.storage_capacity = os.environ.get('_JUPYTERHUB_VOLUME_SIZE')
c.KubeSpawner.volumes = [
    {
        'name': 'data',
        'persistentVolumeClaim': {
            'claimName': c.KubeSpawner.pvc_name_template
        }
    }
]
c.KubeSpawner.volume_mounts = [
    {
        'name': 'data',
        'mountPath': '/opt/app-root/src'
    }
]