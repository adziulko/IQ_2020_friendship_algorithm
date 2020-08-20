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

import sys
import time


def slow_print(text: str, sleep_time: int = 0.025):
    """Print text slowly so we're very fashionable"""
    for char in text:
        time.sleep(sleep_time)
        print(char, end="", flush=True)


def slow_input(prompt: str):
    slow_print(prompt)
    return input()


def y_or_n_p(prompt: str):
    """Basic implementation of y-or-n predicate function in the style of
    lisp-family languages
    """
    while True:
        choice = slow_input(f"{prompt} [y/n]: ")
        if choice == "y":
            return True
        if choice == "n":
            return False
        print("You must select y or n")


def simple_question(
    prompt: str, double_check: bool = False, num_points_to_give: int = 5
):
    """Generic function to handle the simple case of a question where we
    give a fixed number of points for an affirmative answer.

    """
    if y_or_n_p(prompt):
        if double_check:
            if not y_or_n_p("Are you sure about that?"):
                return 0
        return num_points_to_give
    return 0


def multiple_choice(prompt: str, choices: [str], points_per_choice: [int]):
    """Generic function to handle multiple choice questions in the context
    of the quiz.

    """
    if len(choices) != len(points_per_choice):
        raise Exception("choices and points_per_choice must have same length")
    formatted_choices = "\n".join(
        [f"{k+1}: {v}" for k, v in enumerate(choices)]
    )
    prompt_text = f"{prompt}\n{formatted_choices}\n"
    while True:
        choice = int(slow_input(prompt_text))
        num_choices = len(choices)
        if choice in range(1, num_choices + 1):
            return points_per_choice[choice - 1]
        print(
            f"You must select an option between 1 and {num_choices}, inclusive."
        )


def play_game():
    """Main function that actually runs the game we have defined. We
    choose to wrap each step in an independent function to preserve
    separation of functionality.

    """
    while True:
        user_entry = multiple_choice(
            "Select option:", ("Play Game", "Exit Game"), (1, 2)
        )
        # if the user selects 1, they want to play! Ask them questions and wait for their answers.
        if user_entry == 1:
            points = 0
            points += simple_question("Do you like sourdough bread?")
            points += simple_question(
                "Do you like hiking in the great outdoors?"
            )
            points += simple_question(
                "Do you like dogs?", double_check=True, num_points_to_give=10
            )
            points += multiple_choice(
                "Reading is for:",
                ("People with time", "People with brains", "Cool kids"),
                (0, 5, 10),
            )
            slow_print("Calculating friendship score...\n\n")
            if points > 20:
                slow_print("Best Friends!")
            elif points > 10:
                slow_print("Just Friends...")
            else:
                slow_print("We should get to know each other better...")
            print("\n")

        if user_entry == 2:
            slow_print("Sayonara...")
            sys.exit(0)


if __name__ == "__main__":
    play_game()

#
# Zach_Maas.py ends here
