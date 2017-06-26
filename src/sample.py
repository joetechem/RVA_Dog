
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
                          


def shedding(intent, session):
    session_attributes = {}
    reprompt_text = None
    speech_output = ""
    should_end_session = True
    
    card_output = "Use a hefty brush, like the Furminator. To really keep shedding under control, comb your dog at least once per week."
    speech_output = "<speak>Do you find dog hairs in every nick and cranny? Well. That's the dog life for you! Depending on your dog's breed. Your dog will always shed hairs to make room for new ones. You can handle the amount of hairs. They kindly leave for you by combing your dog at least once a week. The smaller the teeth of the brush, the better. Each brushing session should last at least 10 minutes.</speak>"

    return build_response(session_attributes, build_speechlet_response
                          ("How to Handle Shedding", card_output, speech_output, reprompt_text, should_end_session))

                         
                          


    # Dispatch to skill's intent handlers

    if intent_name == "DogParks":
        return dog_parks(intent, session)
    elif intent_name == "Shedding":
        return trail(intent, session)


