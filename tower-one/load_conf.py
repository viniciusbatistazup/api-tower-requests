import yaml
import os.path
from os import path


def load_yml_file(yml_file):
    if(path.exists(yml_file) is not False):
        with open(yml_file, 'r') as stream:
            try:
                return yaml.safe_load(stream)
            except yaml.YAMLError as exc:
                print(exc)
                return None
    else:
        return None


# print(load_yml_file("conf.yaml"))
