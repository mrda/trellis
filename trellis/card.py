#!/usr/bin/env python
#
# card.py - handle Trello cards
#
# Copyright (C) 2020 Michael Davies <michael@the-davies.net>
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA  02111-1307, USA.
# Or try here: http://www.fsf.org/copyleft/gpl.html

import prettytable

from trellis import command
from trellis import config
from trellis import trello_if
from trellis import utils


class Card:
    """Representation of a Card
    https://developers.trello.com/reference/#card-object
    """

    def __init__(self):
        self.cmd = command.Command('card')
        self.cmd.add('add', self.add, help_text="<card>")
        self.cmd.add('list', self.list,
                     help_text="- List all cards for the current list")

    def add(self, args=None):
        if utils.debug:
            print("Invoking card.add with {}".format(args))
        print("Not yet implemented")

    def list(self, args=None):
        if utils.debug:
            print("Invoking card.list with {}".format(args))
        try:
            table = prettytable.PrettyTable()
            table.field_names = ['id', 'name', 'due', 'due complete',
                                 'short url']
            for f in table.field_names:
                table.align[f] = 'l'

            curr_list_id = config.get_default_list()[0]
            cards = trello_if.get_cards(curr_list_id)
            for card in cards:
                table.add_row([card.id, card.name, card.due,
                              card.is_due_complete, card.shortUrl])
            print(table)
        except Exception as e:
            print("Error: Could not list cards ({})".format(e))
