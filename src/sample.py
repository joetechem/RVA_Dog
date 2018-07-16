"""
Simple Python Lambda function providing helpful tips for dog owners in Richmond, Va.
Intents supported:
    Open
    GetHelp
    Stop
    DogParks
    RecommendPlace
"""

import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

import random
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

    # the text that appears on the Alexa App and the Alexa Show:
    card_output = "Barker Field. Church Hill Dog Park."
    # what Alexa actually says (between the speak tags):
    speech_output = "<speak>Here are several dog parks in Richmond, Virginia...</speak>"

    # rolling out everything in this function:
    # The "Dog Parks in RVA" appears as the card title, on the app and the show
    return build_response(session_attributes, build_speechlet_response
                          ("Dog Parks in RVA", card_output, speech_output, reprompt_text, should_end_session))


def choice_park(intent, session):
    session_attributes = {}
    reprompt_text = None
    speech_output = ""
    should_end_session = True

    card_output = "Bandy Field."
    speech_output = "<speak>A dog park that I would recommend? <say-as interpret-as='interjection'>blast</say-as>. There are so many good ones. If I had to choose one, it would be Bandy Field!</speak>"

    return build_response(session_attributes, build_speechlet_response
                          ("Recommended Dog Park", card_output, speech_output, reprompt_text, should_end_session))



def stop(intent, session):
    session_attributes = {}
    reprompt_text = None
    speech_output = ""
    should_end_session = True
    
    card_output = "Have a nice day! Woof! Woof! Bark!"
    speech_output = "<speak>Thank you for asking Richmond Dog Info. Have a nice day! <say-as interpret-as='interjection'>woof!</say-as>.<say-as interpret-as='interjection'>woof!</say-as>.</speak>"

    return build_response(session_attributes, build_speechlet_response
                          ("Session Ended", card_output, speech_output, reprompt_text, should_end_session))
                          
# This function is not actually called. Rather,
# the stop() function above replaces this one
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
    
###### EDIT CARD TITLE, CARD OUTPUT, SPEECH OUTPUT ######
    # Dispatch to skill's launch
    return build_response({},build_speechlet_response(
        "Richmond Dog Info", "Welcome to the Amazon Alexa skill, Richmond Dog Info!", "<speak>Welcome to the Amazon Alexa skill, Richmond Dog Info. If you're not sure where you can take your dog in Richmond, Virginia. Just ask me! There are plenty of places and things to do in and around the city! From festivals, events, dog parks, breweries, trails and swimming spots. I also share some great information on common dog questions.</speak>","",False))
         # CARD TITLE        # CARD OUTPUT                                             # SPEECH OUTPUT: WHAT ALEXA ACTUALLY SAYS WHEN THE SKILL IS FIRST OPENED

# List of example intents to return when get_help() is called
# Randomly selects a phrase from the list, example_intents
example_intents = [
    "dog-friendly breweries, festivals, or events.",
    "dog parks, or one I'd recommend.",
    "where to take  hiking and running trails.",
    "how to remove a dog tick.",
    "why does my dog eat grass.",
    "why does my dog bury bones and other stuff.",
    "tips to handle dog shedding."
    ]

###### Another function made to make the Help intent a little better ####
def get_help(intent, session):
    """ Called when the user asks for help """
    session_attributes = {}
    reprompt_text = None
    speech_output = ""
    should_end_session = False
    
    card_output = "You can ask Richmond Dog Info: What dog parks are in Richmond? Dog-friendly breweries, festivals, or events? Where can I take my dog to swim or hike? Why does my dog eat grass? Why does my dog bury bones? How can I handle shedding or remove a tick?"
    speech_output = "<speak>You can ask me about " + random.choice(example_intents) + " </speak>"

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
    elif intent_name == "Stop":
        return stop(intent, session)
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
