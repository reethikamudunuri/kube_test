from kubernetes import client, config

class Pod(object):
    def __init__(self):
        config.load_kube_config()
        v1 = client.CoreV1Api()
        self.pods = v1.list_pod_for_all_namespaces(watch=False)

    def get_images(self,pod):
        images = []
        for i in pod.spec.containers:
            images.append(i.image)
        return images
