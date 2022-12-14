import Faraz_Module5
import random

def init():
    initializationResponses = [
            "Hi! I'm Faraz! Tell me how can I help?",
            "Hello! How may I help you?",
            "Hi! Good to see you, How can I help?",
            "Hello, So nice to meet you, please tell me your question:",
            "Hey! How have you been? I'm listening!",
            "Pleasure to meet you, please tell me how can I help?"
     ]    
    # a random number between 0 and len of initializationResponses list
    rnd = random.randint(0, len(initializationResponses) - 1)
    Faraz_Module5.speechSynthesis(initializationResponses[rnd])
    
    
    
def terminate():
    terminateResponses = [
            "That was so nice to talk to you! Bye",
            "Please let me know if you have any other questions",
            "Thanks for your question!",
            "See you soon! Bye!"
     ]
    # a random number between 0 and len of terminateResponses list
    rnd = random.randint(0, len(terminateResponses) - 1)
    Faraz_Module5.speechSynthesis(terminateResponses[rnd])