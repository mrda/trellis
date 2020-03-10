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


class TrellisList:
    """Representation of a List"""

    def __init__(self):
        self.cmd = command.Command('list')
        self.cmd.add('set', self.set,
                     help_text=" <list> - Set a default list")
        self.cmd.add('list', self.list, help_text="- List available lists")

    def default(self):
        if utils.debug:
            print("Invoking list default func")
        try:
            print(' '.join("'{}'".format(f) for f in
                  config.get_default_list()))
        except Exception as e:
            print("Error: Could not get default list.  Have you set one?")

    def set(self, args):
        if utils.debug:
            print("Invoking list.set with {}".format(args))
        if len(args) != 1:
            print("Error: 'set' takes one parameter, the list name or id")
            return
        try:
            search_list = args[0]
            found_list = None

            board_meta = config.get_default_board()
            board_obj = trello_if.get_board(board_meta[0])

            for tlist in board_obj.all_lists():
                if search_list in [tlist.id, tlist.name]:
                    found_list = tlist

            if found_list is None:
                print("Error: Could not match '{}' against your list of lists"
                      .format(search_list))
                return
            config.set_default_list(found_list.id, found_list.name)

        except Exception as e:
            print("Error: Could not set default list ({})".format(e))

    def list(self, args=None):
        if utils.debug:
            print("Invoking list.list with {}".format(args))
        try:
            board_meta = config.get_default_board()
            board_obj = trello_if.get_board(board_meta[0])

            table = prettytable.PrettyTable()
            table.field_names = ['id', 'name']
            for f in table.field_names:
                table.align[f] = 'l'

            for lst in board_obj.all_lists():
                if not lst.closed:
                    table.add_row([lst.id, lst.name])
            print("Board: {}".format(board_meta[1]))
            print(table)
        except Exception as e:
            print("Error: Could not list all lists for board ({})".format(e))
