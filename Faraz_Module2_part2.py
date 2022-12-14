# ////////// Second module - Part 2 //////////
# ////////// Intent Detections and Slot Filling //////////

# How to load? 
# https://snips-nlu.readthedocs.io/en/latest/tutorial.html#persisting

from snips_nlu import SnipsNLUEngine

def IntentDetection_SlotFilling(query):
    loaded_engine = SnipsNLUEngine.from_path("Faraz_nlu_engine")
    parsedQuery = loaded_engine.parse(query)    
    #print(parsedQuery)
    intent, slots = parsedQuery["intent"]["intentName"], parsedQuery['slots'][0]['value']['value']
    return (intent, slots)