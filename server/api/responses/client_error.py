def bad_request(field):
    response = {
        "message": "The {field} value is required.".format(field=field)
    }

    return response, 400


def not_host():
    response = {
        "message": "The player making the request is not the host."
    }

    return response, 400


def not_enough_players():
    response = {
        "message": "The game does not have enough players to start."
    }

    return response, 400


def enough_players():
    response = {
        "message": "The game already has enough players to start."
    }

    return response, 400


def not_found(item="item", plural=False):
    message = "The requested {item} is not found or does not exist.".format(item=item)

    if plural:  # check if message needs to be plural
        message = "The requested {item} are not found or do not exist.".format(item=item)

    response = {
        "message": message
    }

    return response, 404


def conflict(field):
    response = {
        "message": "The {field} value causes issues.".format(field=field)
    }

    return response, 409
