# ////////// YAML to JSON //////////
# ////////// This will be used in  //////////

# Source for converting YAML to JSON: https://youtu.be/L433MPex178
# pip install ruamel.yaml

import json
from ruamel.yaml import YAML

def conversion(in_file, out_file):
    # create yaml object:
    yaml = YAML()

    with open(in_file, "r") as i:
        data = yaml.load(i)
    
    with open(out_file, "w") as o:
        json.dump(data, o, indent = 4, ensure_ascii = False)
