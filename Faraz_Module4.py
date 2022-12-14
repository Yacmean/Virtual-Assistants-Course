# ////////// Fourth module //////////
# ////////// Answer Generation //////////

import random
def weatherPotentialResponses (slots, answers):
    weatherReponses = [
            "Today, {city}'s weather is {weather} and it's {degrees} degrees".format(city = slots, weather = answers[0], degrees = answers[1]),
            "Hmmm! It seems that {city} is {weather} today, and it feels like {degrees} degrees".format(city = slots, weather = answers[0], degrees = answers[1]),
            "{city} is {degrees} degrees and {weather}.".format(city = slots, weather = answers[0], degrees = answers[1]),
            "Oh! It's {weather} now with {degrees} degrees".format(city = slots, weather = answers[0], degrees = answers[1]),
            "{city} is {weather} today with {degrees} degrees!".format(city = slots, weather = answers[0], degrees = answers[1])
            ]

    # a random number between 0 and weatherReponses list
    rnd = random.randint(0, len(weatherReponses) - 1)
    return weatherReponses[rnd]


def NLG(intent, slots, answers):
    if (intent == "Weather"):
        return weatherPotentialResponses(slots, answers)   
