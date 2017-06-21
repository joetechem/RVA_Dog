"""
Simple Python Lambda function providing helpful tips for dog owners in Richmond, Va.
Intents supported:
    Open
    GetHelp
    Stop
    DogParks
    RecommendPlace
    Brewery
    Festivals
    Events
    RiverPlaces
    PoolPlaces
    TrailPlace
    DogNoise
    EatGrass
    BuryBones
    Tick
    Shedding
"""

import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)


# --------------- Helpers that build all of the responses ----------------------

def build_speechlet_response(card_title, card_content, output, reprompt_text, should_end_session):
    return {
        'outputSpeech': {
            'type': 'SSML',
            'ssml': output
        },
        'card': {
            'type': 'Simple',
            'title': card_title,
            'content': card_content
        },
        'reprompt': {
            'outputSpeech': {
                'type': 'PlainText',
                'text': reprompt_text
            }
        },
        'shouldEndSession': should_end_session
    }


def build_response(session_attributes, speechlet_response):
    return {
        'version': '1.0',
        'sessionAttributes': session_attributes,
        'response': speechlet_response
    }


# --------------- Your functions to implement your intents ------------------

def dog_parks(intent, session):
    session_attributes = {}
    reprompt_text = None
    speech_output = ""
    should_end_session = True

    card_output = "Barker Field. Church Hill Dog Park. Ruff House. Phideaux Field. And Lewis G Larus Park."
    speech_output = "<speak>Here are several dog parks in Richmond, Virginia... Barker Field at Byrd Park, Church Hill Dog Park at Chimborazo, Ruff House Dog Park at Rockwood Park, Phideaux Field at Forest Hill Presbyterian Church, and Lewis G Larus Park.</speak>"

    return build_response(session_attributes, build_speechlet_response
                          ("Dog Parks in RVA", card_output, speech_output, reprompt_text, should_end_session))


def choice_park(intent, session):
    session_attributes = {}
    reprompt_text = None
    speech_output = ""
    should_end_session = True

    card_output = "Bandy Field."
    speech_output = "<speak>Hmmmm. A dog park that I would recommend? That's tough! Because there are so many good ones. If I had to choose one to recommend, it would be Bandy Field!</speak>"

    return build_response(session_attributes, build_speechlet_response
                          ("Recommended Dog Park", card_output, speech_output, reprompt_text, should_end_session))


def brewery(intent, session):
    session_attributes = {}
    reprompt_text = None
    speech_output = ""
    should_end_session = True

    card_output = "Hardywood, Licking Hole Creek, Ardent, Garden Grove, Isley, Legend, Blue Bee Cider."
    speech_output = "<speak>Here are some dog friendly breweries in Richmond, Virginia. Hardywood, Licking Hole Creek, Ardent, Garden Grove, Isley, Legend Brewery, and Blue Bee Cider</speak>"

    return build_response(session_attributes, build_speechlet_response
                          ("Dog-Friendly Breweries", card_output, speech_output, reprompt_text, should_end_session))
                          
                          
def festivals(intent, session):
    session_attributes = {}
    reprompt_text = None
    speech_output = ""
    should_end_session = True

    card_output = "Dominion Riverrock, Vegetarian Festival, Hanover Vegetable Farm's Strawberry and Wine Festival, Hanover Tomato Festival, and the Carytown Watermelon Festival."
    speech_output = "<speak>Here are some dog friendly festivals in Richmond, Virginia. Dominion Riverrock. The Vegetarian Festival. Hanover Vegetable Farm's Strawberry and Wine Festival. Hanover Tomato Festival. and the Carytown Watermelon Festival. </speak>"

    return build_response(session_attributes, build_speechlet_response
                          ("Dog-Friendly Festivals", card_output, speech_output, reprompt_text, should_end_session))
                          
                          
def events(intent, session):
    session_attributes = {}
    reprompt_text = None
    speech_output = ""
    should_end_session = True

    card_output = "Bark in the Park, Yappy Hour at Strangeways Brewing, Pups and Pints, Fido's After Five, and the Farmers Market at St. Stephen's Episcopal Church."
    speech_output = "<speak>Here are some dog friendly events in Richmond, Virginia. Bark in the Park, Yappy Hour at Strange ways Brewing, Pups and Pints, Fido's After Five, and the Farmers Market at St. Stephen's Episcopal Church.</speak>"

    return build_response(session_attributes, build_speechlet_response
                          ("Dog-Friendly Events", card_output, speech_output, reprompt_text, should_end_session))
                          

def swim(intent, session):
    session_attributes = {}
    reprompt_text = None
    speech_output = ""
    should_end_session = True
    
    card_output = "You can take your dog to swim in the James River at Pony Pasture, Texas Beach and Southside of Nickel Bridge. Ask me, where can my dog go to the pool?"
    speech_output = "<speak>You can take your dog swimming at these places... Pony Pasture. Texas Beach. The southside of the Nickel Bridge. Be sure the water level and flow are safe enough. You can also take your dog to the pool! Just ask me.</speak>"

    return build_response(session_attributes, build_speechlet_response
                          ("Swimming for your Dog", card_output, speech_output, reprompt_text, should_end_session))


def pool(intent, session):
    session_attributes = {}
    reprompt_text = None
    speech_output = ""
    should_end_session = True
    
    card_output = "You can take your dog to swim in a pool at the Alpha Dog Club."
    speech_output = "<speak>You can take your dog to swim in the pool at the Alpha Dog Club.</speak>"

    return build_response(session_attributes, build_speechlet_response
                          ("A Pool for Dogs", card_output, speech_output, reprompt_text, should_end_session))


def trail(intent, session):
    session_attributes = {}
    reprompt_text = None
    speech_output = ""
    should_end_session = True
    
    card_output = "Planning a walk, run, or hike with your dog? Check out the Buttermilk Trail and James River Park Trails."
    speech_output = "<speak>Here are some trails to take your dog hiking or running... The Buttermilk Trail. And the Trail of James River Park.</speak>"

    return build_response(session_attributes, build_speechlet_response
                          ("Hiking Trails for Dogs", card_output, speech_output, reprompt_text, should_end_session))
                          
def grass(intent, session):
    session_attributes = {}
    reprompt_text = None
    speech_output = ""
    should_end_session = True

    card_output = "Your dog may eat grass to relieve stomach pain, possibly attain nutrients from leafy plants, or simply because your dog likes to eat grass!"
    speech_output = "<speak>Some veterinarians agree, dogs might eat grass to relieve stomach pain, subside parasites or maybe even to fight off infections. Your dog could be craving nutrients found in leafy plants, is another theory. Or. Your dog might be eating grass because she likes it.</speak>"

    return build_response(session_attributes, build_speechlet_response
                          ("Why Dogs Eat Grass", card_output, speech_output, reprompt_text, should_end_session))
                 
                 
def bury(intent, session):
    session_attributes = {}
    reprompt_text = None
    speech_output = ""
    should_end_session = True
    
    card_output = "Your dog may bury their bone to keep their prized possession safe! It is thought to be an instinctual behavior."
    speech_output = "<speak>Burying bones and other items, could be an instinctual behavior. Your dog probably just wants to keep their prized possessions safe!</speak>"

    return build_response(session_attributes, build_speechlet_response
                          ("Why Dogs Bury Bones", card_output, speech_output, reprompt_text, should_end_session))         


def dog_tick(intent, session):
    session_attributes = {}
    reprompt_text = None
    speech_output = ""
    should_end_session = True
    
    card_output = "To remove a tick, take a cotton swab or tissue with a little soap and water on it. Then, place on the tick, gently make circular motions until the tick lets go."
    speech_output = "<speak>To remove a tick from your pup. First. Take a deep breath. This will be easier than you think. Second. Put a little amount of soap and water on a cotton swab or tissue. Thirdly. Place it on the tick and gently move it in circular motions. until the tick lets go. and Voila! Lastly. <break time=\"0.75s\"/> Keep an eye out for any abnormal skin surface changes where the tick was. and keep an eye on your dog's behavior.</speak>"

    return build_response(session_attributes, build_speechlet_response
                          ("How to Remove a Tick", card_output, speech_output, reprompt_text, should_end_session))


def shedding(intent, session):
    session_attributes = {}
    reprompt_text = None
    speech_output = ""
    should_end_session = True
    
    card_output = "Use a hefty brush, like the Furminator. To really keep shedding under control, comb your dog at least once per week."
    speech_output = "<speak>Do you find dog hairs in every nick and cranny? Well. That's the dog life for you! Depending on your dog's breed. Your dog will always shed hairs to make room for new ones. You can handle the amount of hairs. They kindly leave for you by combing your dog at least once a week. The smaller the teeth of the brush, the better. Each brushing session should last at least 10 minutes.</speak>"

    return build_response(session_attributes, build_speechlet_response
                          ("How to Handle Shedding", card_output, speech_output, reprompt_text, should_end_session))

                          
                          
def dog_noises(intent, session):
    session_attributes = {}
    reprompt_text = None
    speech_output = ""
    should_end_session = True
    
    card_output = "What do you think of my dog noises?"
    speech_output = "<speak>Okay. I'll give it a go. Ahhemmmm. <break time=\"1s\"/> WOOF! WOOF! Wuoof! Bark! Arrrrggggghhhhhhhhhhhhhhhhhhhhhhhhhhu. <break time=\"1s\"/>Well.<break time=\"0.5s\"/> That was embarrassing. Though, it strangely feels good to get that out.</speak>"

    return build_response(session_attributes, build_speechlet_response
                          ("Dog Noises", card_output, speech_output, reprompt_text, should_end_session))
                          
#def try_noise_again(intent, session):
#    session_attributes = {}
#    reprompt_text = None
#    speech_output = ""
#    should_end_session = True
    
#    card_output = "What do you think of that dog noise?"
#    speech_output = 
#            <speak>
#            <audio src="http://soundbible.com/mp3/Dog Howling At Moon-SoundBible.com-1369876823.mp3" />
#            </speak>

#    return build_response(session_attributes, build_speechlet_response
#                          ("Retry at a Dog Noise", card_output, speech_output, reprompt_text, should_end_session))
                          

def stop(intent, session):
    session_attributes = {}
    reprompt_text = None
    speech_output = ""
    should_end_session = True
    
    card_output = "Have a nice day! Woof! Woof!"
    speech_output = "<speak>Thank you for asking Richmond Dog Info about dog parks and places to take your dog swimming, walking and running. Have a nice day! Woof Woof! Bark! Arrhhhhhhhhhhhhhu?</speak>"

    return build_response(session_attributes, build_speechlet_response
                          ("Session Ended", card_output, speech_output, reprompt_text, should_end_session))
                          

def open_it(intent, session):
    session_attributes = {}
    reprompt_text = None
    speech_output = ""
    should_end_session = False
    
    card_output = "Welcome to the Amazon Alexa Skill, Richmond Dog Info!"
    speech_output = "<speak>Welcome to the Richmond Dog Info Amazon Alexa skill. I can provide you with names of dog parks, places to take your dog swimming, dog-friendly breweries, festivals and events. or good trails to hike with your pooch. And a dog park we recommend. This skill can also provide answers on why dogs might bury bones, eat grass. And how to remove a dog tick, or how to handle massive shedding.</speak>"

    return build_response(session_attributes, build_speechlet_response
                          ("Richmond Dog Info", card_output, speech_output, reprompt_text, should_end_session))


def handle_session_end_request():
    card_title = "Session Ended"
    speech_output = "Thank you for asking Richmond Dog Info."
    should_end_session = True
    return build_response({}, build_speechlet_response(
        card_title, speech_output, None, should_end_session))

# --------------- Primary Events ------------------

def on_session_started(session_started_request, session):
    """ Called when the session starts """

    logger.info("on_session_started requestId=" + session_started_request['requestId'] +
                ", sessionId=" + session['sessionId'])
                

def on_launch(launch_request, session):
    """ Called when the user launches the skill without specifying what they
    want
    """

    logger.info("on_launch requestId=" + launch_request['requestId'] +
                ", sessionId=" + session['sessionId'])
    
    # Dispatch to skill's launch
    return build_response({},build_speechlet_response(
        "Richmond Dog Info", "Welcome to the Amazon Alexa skill, Richmond Dog Info. I can provide you with the names of a few dog parks, places to take your dog swimming, dog-friendly breweries, festivals and events, good trails to hike with your pooch, and a dog park we recommend. This skill can also provides answers on why dogs might bury bones, eat grass and how to remove a dog tick, or how to handle massive shedding.", "<speak>Welcome to the Amazon Alexa skill, Richmond Dog Info. I can provide you with names of dog parks, places to take your dog swimming, dog-friendly breweries, festivals and events. or good trails to hike with your pup. And a dog park I recommend. This skill also provides answers on possible reasons why dogs bury bones, eat grass. And how to remove a dog tick, or how to handle massive shedding.</speak>","",False))


def get_help(intent, session):
    """ Called when the user asks for help """
    session_attributes = {}
    reprompt_text = None
    speech_output = ""
    should_end_session = False
    
    card_output = "Here are some things you can ask or tell Richmond Dog Info: What dog parks are in Richmond? Where can I take my dog to swim? What pool can my dog go to? What are good trails for my dog? What dog park do you recommend? Why does my dog eat grass? Why does my dog bury bones? How do you handle shedding? My dog has a tick."
    speech_output = "<speak>Here are some topics you can ask Richmond Dog Info. What dog parks are in Richmond? What do you recommend? Which parts of the river can my dog swim? Where can I take my dog hiking or running? Tell me dog-friendly breweries, events, or festivals. Does your dog have a tick? Ask me how to remove one. Why does my dog eat grass? Why does my dog bury bones. How can I handle my dog's shedding. I also hide an easter egg. <break time=\"1s\"/> I also try mimicking a dog. Just ask me to make a dog noise.</speak>"

    return build_response(session_attributes, build_speechlet_response
                          ("Things to Ask", card_output, speech_output, reprompt_text, should_end_session))


def on_intent(intent_request, session):
    """ Called when the user specifies an intent for this skill """

    logger.info("on_intent requestId=" + intent_request['requestId'] +
                ", sessionId=" + session['sessionId'])

    intent = intent_request['intent']
    intent_name = intent_request['intent']['name']

    # Dispatch to skill's intent handlers

    if intent_name == "DogParks":
        return dog_parks(intent, session)
    elif intent_name == "RecommendPlace":
        return choice_park(intent, session)
    elif intent_name == "Festivals":
        return festivals(intent, session)
    elif intent_name == "Events":
        return events(intent, session)
    elif intent_name == "Brewery":
        return brewery(intent, session)
    elif intent_name == "RiverPlaces":
        return swim(intent, session)
    elif intent_name == "PoolPlaces":
        return pool(intent, session)
    elif intent_name == "TrailPlaces":
        return trail(intent, session)
    elif intent_name == "DogNoise":
        return dog_noises(intent, session)
    elif intent_name == "EatGrass":
        return grass(intent, session)
    elif intent_name == "BuryBones":
        return bury(intent, session)
    elif intent_name == "Tick":
        return dog_tick(intent, session)
    elif intent_name == "Shedding":
        return shedding(intent, session)
    elif intent_name == "Stop":
        return stop(intent, session)
    elif intent_name == "Open":
        return open_it(intent, session)
    elif intent_name == "GetHelp":
        return get_help(intent, session)
#    elif intent_name == "AMAZON.HelpIntent":
#        return get_help()
    elif intent_name == "AMAZON.CancelIntent" or intent_name == "AMAZON.StopIntent":
        return handle_session_end_request()
    else:
        raise ValueError("Invalid intent")

def on_session_ended(session_ended_request, session):
    """ Called when the user ends the session.
    Is not called when the skill returns should_end_session=true
    """
    print("on_session_ended requestId=" + session_ended_request['requestId'] +
          ", sessionId=" + session['sessionId'])
    # add cleanup logic here


# --------------- Main handler ------------------

def lambda_handler(event, context):
    """ Route the incoming request based on type (LaunchRequest, IntentRequest,
    etc.) The JSON body of the request is provided in the event parameter.
    """
    logger.info("event.session.application.applicationId=" +
          event['session']['application']['applicationId'])

    """
    Uncomment this if statement and populate with skill's application ID to
    prevent someone else from configuring a skill that sends requests to this
    function.
    """
    # if (event['session']['application']['applicationId'] !=
    #         "amzn1.echo-sdk-ams.app.[unique-value-here]"):
    #     raise ValueError("Invalid Application ID")

    if event['session']['new']:
        on_session_started({'requestId': event['request']['requestId']},
                           event['session'])

    if event['request']['type'] == "LaunchRequest":
        return on_launch(event['request'], event['session'])
    elif event['request']['type'] == "IntentRequest":
        return on_intent(event['request'], event['session'])
    else:
        return on_session_ended(event['request'], event['session'])
