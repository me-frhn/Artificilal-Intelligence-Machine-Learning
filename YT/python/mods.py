# ============================================================
# CODEX: Built-in Modules
# ============================================================

# Import the built-in random module
# Used to generate random numbers or randomly select items
import random

# Import the built-in datetime module
# Used to work with dates and time
import datetime

# Import the built-in os module
# Used to interact with the operating system
import os

import pandas as pd

# ------------------------------------------------------------
# random.randint(start, end)
# Generates a random integer between start and end
# Both start and end values are included
#
# Example:
# random.randint(1, 10) → can return any number from 1 to 10
# ------------------------------------------------------------

# num = random.randint(1, 10)


# ------------------------------------------------------------
# random.choice(sequence)
# Randomly selects and returns one item from a sequence
# such as a list, tuple, or string
# ------------------------------------------------------------

# choice = random.choice(["apple", "mango", "banana"])


# Print the randomly generated number
# print(num)

# Print the randomly selected item
# print(choice)


# ------------------------------------------------------------
# datetime.date.today()
# Returns today's current date
#
# Example output:
# 2026-08-21
# ------------------------------------------------------------

# today = datetime.date.today()
# print(today)


# ------------------------------------------------------------
# os.getcwd()
# getcwd = Get Current Working Directory
# Returns the path of the folder where the Python program
# is currently running
# ------------------------------------------------------------

# current_dir = os.getcwd()

# print(current_dir)