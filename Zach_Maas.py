# Zach_Maas.py --- Zach Maas' Friendship Algorithm Project
#
# Filename: Zach_Maas.py
# Author: Zachary Maas <zama8258@colorado.edu>
# Created: Thu Aug 20 16:17:36 2020 (-0600)
#
#

# Commentary:
#
#
# This file contains the code required for Zach Maas' version of the
# 'Friendship Algorithm' project created for an IQ biology workshop on
# Thu 20 Aug 2020. This project demonstrates basic python programming
# skills and was also used to provide a basic example to learn how to
# work with git collaboration effectively.
#
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or (at
# your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with GNU Emacs.  If not, see <https://www.gnu.org/licenses/>.
#
#

# Code:


## Function to play friendship algorithm game
def play_game():
    ## START GAME

    # initialize the user input to 0
    user_entry = 0
    # ask the user to make their own input (1 to play or 2 to exit):
    while user_entry != 1 and user_entry != 2:
        user_entry = input(
            "Select Option!\n1. Play Game\n2. Exit Game\n\nYour Selection: "
        )
    # if the user selects 1, they want to play! Ask them questions and wait for their answers.
    while user_entry == 1:
        ## STEP 1 HERE

        ## STEP 2&3 HERE

        ## STEP 4 HERE

        user_entry = input(
            "Select Option!\n1. Play Game\n2. Exit Game\n\nYour Selection: "
        )
        user_entry = int(user_entry)


## Function call to play friendship algorithm game
play_game()

#
# Zach_Maas.py ends here
