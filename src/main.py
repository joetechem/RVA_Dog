"""
Simple Python Lambda function providing helpful tips for dog owners in Richmond, Va.
Intents supported:
    Open
    GetHelp
    Stop
    DogParks
    RecommendPlace
    RiverPlaces
    PoolPlaces
    TrailPlaces
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
                          ("RVA Dog Parks", card_output, speech_output, reprompt_text, should_end_session))


def choice_park(intent, session):
    session_attributes = {}
    reprompt_text = None
    speech_output = ""
    should_end_session = True

    card_output = "Bandy Field."
    speech_output = "<speak>Hmmmm. A dog park that I would recommend? Well, that would be Bandy Field!</speak>"

    return build_response(session_attributes, build_speechlet_response
                          ("Recommended Dog Park", card_output, speech_output, reprompt_text, should_end_session))


def swim(intent, session):
    session_attributes = {}
    reprompt_text = None
    speech_output = ""
    should_end_session = True
    
    card_output = "You can take your dog to swim in the James River at Pony Pasture, Texas Beach and Southside of Nickel Bridge. Ask me, where can my dog go to the pool?"
    speech_output = "<speak>You can take your dog swimming at these places... Pony Pasture. Texas Beach. The southside of the Nickel Bridge. Be sure the water level and flow are safe enough. You can also take your dog to the pool! Just ask me.</speak>"

    return build_response(session_attributes, build_speechlet_response
                          ("Where your Dog can Swim", card_output, speech_output, reprompt_text, should_end_session))


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
    speech_output = "<speak>Here are some trails you can take your dog... The Buttermilk Trail. And the Trail of James River Park.</speak>"

    return build_response(session_attributes, build_speechlet_response
                          ("Dog Hiking Trails", card_output, speech_output, reprompt_text, should_end_session))
                          
def dog_noises(intent, session):
    session_attributes = {}
    reprompt_text = None
    speech_output = ""
    should_end_session = True
    
    card_output = "What do you think of my dog noises?"
    speech_output = "<speak>Okay. I'll give it a go. Ahhemmmm. <break time=\"1s\"/> WOOF! WOOF! Arrrrggggghhhhhhhhhhhhhhhhhhhhhhhhhhu. <break time=\"1s\"/>Well.<break time=\"0.5s\"/> That was embarrassing. Though, it feels good to get that out.</speak>"

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
    
    card_output = "Have a nice day! Woof!"
    speech_output = "<speak>Thank you for asking Koa Dog RVA about dog parks and places to take your dog swimming, walking and running. Have a nice day! Woof Woof! Bark! Arrhhhhhhhhhhhhhu!</speak>"

    return build_response(session_attributes, build_speechlet_response
                          ("Session Ended", card_output, speech_output, reprompt_text, should_end_session))
                          

def open_it(intent, session):
    session_attributes = {}
    reprompt_text = None
    speech_output = ""
    should_end_session = False
    
    card_output = "Welcome to the RVA Dog Amazon Alexa Skill"
    speech_output = "<speak>Welcome to the Koa Dog RVA skill. I can provide you with information about dog parks, places to take your dog swimming, or good trails to hike with your pooch. And a dog park I would recommend.</speak>"

    return build_response(session_attributes, build_speechlet_response
                          ("RVA Dog", card_output, speech_output, reprompt_text, should_end_session))


def handle_session_end_request():
    card_title = "Session Ended"
    speech_output = "Thank you for asking RVA Dog."
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
        "RVA Dog", "Welcome to the RVA Dog skill. I can provide you with information about dog parks, places to take your dog swimming, or good trails to hike with your pooch. And a dog park I would recommend.","<speak>Welcome to the RVA Dog skill. I can provide you with information about dog parks, places to take your dog swimming, or good trails to hike with your pooch. And a dog park I would recommend.</speak>","",False))


def get_help(intent, session):
    """ Called when the user asks for help """
    session_attributes = {}
    reprompt_text = None
    speech_output = ""
    should_end_session = False
    
    card_output = "Here are some things you can ask or tell RVA Dog: What dog parks are in Richmond? Where can I take my dog to swim? What are some good trails for my dog? What dog park do you recommend?"
    speech_output = "<speak>Need help navigating RVA Dog? Here are some keywords RVA Dog understands. What dog parks are in Richmond? Where can I take my dog to swim? What are some good trails for my dog? What dog park do you recommend?</speak>"

    return build_response(session_attributes, build_speechlet_response
                          ("How to RVA Dog", card_output, speech_output, reprompt_text, should_end_session))


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
    elif intent_name == "RiverPlaces":
        return swim(intent, session)
    elif intent_name == "PoolPlaces":
        return pool(intent, session)
    elif intent_name == "TrailPlaces":
        return trail(intent, session)
    elif intent_name == "DogNoise":
        return dog_noises(intent, session)
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
