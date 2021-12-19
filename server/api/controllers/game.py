import logging, traceback

from api.classes import card, game

from api.models.game import Game as game_db
from api.models.settings import Settings as settings_db
from api.models.deck_districts import DeckDistricts as deck_districts_db
from api.models.deck_characters import DeckCharacters as deck_characters_db

import api.responses as responses

from api.services import database

from api.utils import helpers

from pprint import pprint


def get_games(sort_order, limit, offset):
    try:
        return

    except Exception:
        logging.error(traceback.format_exc())
        return responses.internal_server_error()


def get_game(game_uuid):
    try:
        return

    except Exception:
        logging.error(traceback.format_exc())
        return responses.internal_server_error()


def create_game(name, description):
    try:
        game_object = game.ClassGame(helpers.create_uuid(), helpers.create_timestamp(), name, description)

        success_write_game = database.write_row_to_db(game_db(
            uuid=game_object.uuid,
            created=game_object.created,
            name=game_object.name,
            description=game_object.description,
            amount_players=game_object.amount_players,
            characters_unused=game_object.characters_unused,
            characters_per_player=game_object.characters_per_player,
            eight_districts_built=game_object.eight_districts_built,
            round=game_object.round))

        if not success_write_game:
            return responses.internal_server_error()

        success_write_settings = database.write_row_to_db(settings_db(
            uuid=helpers.create_uuid(),
            min_players=game_object.settings.min_players,
            max_players=game_object.settings.max_players,
            amount_starting_hand=game_object.settings.amount_starting_hand,
            amount_starting_coins=game_object.settings.amount_starting_coins,
            game_uuid=game_object.uuid))

        if not success_write_settings:
            return responses.internal_server_error()

        game_object.deck_districts = card.ClassCard().get_districts(False)

        success_write_deck_districts = []
        for district in game_object.deck_districts:
            success_write_deck_districts.append(database.write_row_to_db(deck_districts_db(
                uuid=helpers.create_uuid(),
                name=district.card.name,
                amount=district.amount,
                game_uuid=game_object.uuid)))

        if False in success_write_deck_districts:
            return responses.internal_server_error()

        game_object.deck_characters = card.ClassCard().get_characters()

        success_write_deck_characters = []
        for character in game_object.deck_characters:
            success_write_deck_characters.append(database.write_row_to_db(deck_characters_db(
                uuid=helpers.create_uuid(),
                name=character.name,
                game_uuid=game_object.uuid)))

        return responses.db_success_uuid(game_object.uuid)

    except Exception:
        logging.error(traceback.format_exc())
        return responses.internal_server_error()


def join_game(game_uuid):
    try:
        return

    except Exception:
        logging.error(traceback.format_exc())
        return responses.internal_server_error()
