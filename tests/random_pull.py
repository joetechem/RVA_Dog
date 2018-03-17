# A test to randomly pull an intent item from a list of intents
# with the output having the proper <speak> tags

import random

example_intents = [
    "dog-friendly breweries, festivals, or events.",
    "dog parks, or one I'd recommend.",
    "where to take  hiking and running trails.",
    "how to remove a dog tick.",
    "why does my dog eat grass.",
    "why does my dog bury bones and other stuff.",
    "tips to handle dog shedding."
    ]

def main():
    speech_output = "<speak>You can ask me about " + random.choice(example_intents) + " </speak>"
    print speech_output

main()
