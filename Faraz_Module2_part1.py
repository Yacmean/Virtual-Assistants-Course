# ////////// Second module - Part 1 //////////
# ////////// Training the engine //////////


# https://snips-nlu.readthedocs.io/en/latest/index.html
# https://snips-nlu.readthedocs.io/en/latest/quickstart.html
# pip install snips-nlu

import io
import json
from snips_nlu import SnipsNLUEngine
from snips_nlu.default_configs import CONFIG_EN

# This engine is the one you will train and use for parsing.
nlu_engine = SnipsNLUEngine(config = CONFIG_EN)

# The dataset is in YAML format, yet it is needed to be converted to JSON format.
# Write in terminal:
    # snips-nlu generate-dataset en Faraz_weather_dataset.yaml > Faraz_final_dataset.json
with io.open("Faraz_final_dataset.json") as f:
    dataset = json.load(f)

# Fit dataset
nlu_engine.fit(dataset)

# Persisting the nlu_engine
# How to persist: https://snips-nlu.readthedocs.io/en/latest/tutorial.html#persisting
nlu_engine.persist("Faraz_nlu_engine")
