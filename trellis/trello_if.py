#!/usr/bin/env python
#
# trello_if.py - Interface to Trello
#
# Copyright (C) 2020 Michael Davies <michael@the-davies.net>
#

import os

from trello import TrelloClient


client = TrelloClient(
  api_key=os.environ.get("TRELLO_API_KEY"),
  api_secret=os.environ.get("TRELLO_API_SECRET")
)

# Need to do 2 things:
# 1) copy the key from https://trello.com/app-key into TRELLO_API_KEY
# 2) generate a token from the "Token" link on https://trello.com/app-key and
#    put that into TRELLO_API_SECRET

# TODO(mrda): Check to see if these things are in the environment and prompt
#             the user to do stuff if they're not


def get_boards():
    boards = client.list_boards()
    return boards


def get_board(board_id):
    return client.get_board(board_id)


def get_cards(list_id):
    tlist = client.get_list(list_id)
    return tlist.list_cards()
