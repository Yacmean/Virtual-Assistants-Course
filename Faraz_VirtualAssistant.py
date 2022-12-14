import time
import Faraz_state
import Faraz_Module1
import Faraz_Module2_part2
import Faraz_Module3
import Faraz_Module4
import Faraz_Module5


keyword = "thank you"
# Initialize Faraz
Faraz_state.init()

time.sleep(1)

query = Faraz_Module1.speechRecognition()

while (query != keyword):
    while (query == "Sorry could not recognize your voice!"):
        Faraz_Module5.speechSynthesis("Sorry I could not recognize your voice, Please repeat again!") 
        query = Faraz_Module1.speechRecognition()

    # otherwise
    print("Your query is: {}".format(query))

    intent, slots = Faraz_Module2_part2.IntentDetection_SlotFilling(query)
    #print(intent, slots)

    Faraz_Module5.speechSynthesis(Faraz_Module4.NLG(intent, slots, Faraz_Module3.action_dispatcher(intent, slots)))
    
    time.sleep(2)
    query = Faraz_Module1.speechRecognition()
    
    

# Terminating Faraz
Faraz_state.terminate() 


