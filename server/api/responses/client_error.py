from api.responses.definitions import *


def bad_request(field):
    response = define_message("The {field} value is required.".format(field=field))

    return response, 400


def not_host():
    response = define_message("The player making the request is not the host.")

    return response, 400


def not_king():
    response = define_message("The player making the request is not the king.")

    return response, 400


def not_select_expected():
    response = define_message("The player making the request is not expected to select a character.")

    return response, 400


def not_enough_players():
    response = define_message("The game does not have enough players to start.")

    return response, 400


def enough_players():
    response = define_message("The game already has enough players to start.")

    return response, 400


def already_started():
    response = define_message("The game has already started.")

    return response, 400


def not_selection_phase():
    response = define_message("The game needs to be in the character selection phase.")

    return response, 400


def not_turn_phase():
    response = define_message("The game needs to be in the character turn phase.")

    return response, 400


def same_character():
    response = define_message("The requested character cannot be the same as the character to remove.")

    return response, 400


def not_character():
    response = define_message("The player making the request does not have the expected character.")

    return response, 400


def already_income_received():
    response = define_message("The player making the request has already received the income for this character.")

    return response, 400


def must_receive_income_to_end_turn():
    response = define_message("The player making the request must receive an income before ending the turn of this character.")

    return response, 400


def must_receive_income_to_build():
    response = define_message("The player making the request must receive an income before building a district.")

    return response, 400


def already_cards_drawn():
    response = define_message("The player making the request has already drawn the district cards for this character.")

    return response, 400


def no_cards_drawn():
    response = define_message("The player making the request has not yet drawn the district cards for this character.")

    return response, 400


def no_cards_in_hand():
    response = define_message("The player making the request has no district cards their hand.")

    return response, 400


def already_in_city():
    response = define_message("The player making the request already has the same district in their city.")

    return response, 400


def already_completed_city():
    response = define_message("The player making the request already has a completed city.")

    return response, 400


def building_limit():
    response = define_message("The player making the request has reached the building limit for this character.")

    return response, 400


def not_enough_coins():
    response = define_message("The player making the request does not have enough coins to build the district.")

    return response, 400


def not_found(item="item", plural=False):
    message = "The requested {item} is not found or does not exist.".format(item=item)

    if plural:  # check if message needs to be plural
        message = "The requested {item} are not found or do not exist.".format(item=item)

    response = define_message(message)

    return response, 404


def conflict(field):
    response = define_message("The {field} value causes issues.".format(field=field))

    return response, 409
