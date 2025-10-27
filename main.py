# ==================================================================== #
#  File: main.py                                                       #       
#  Author: Ismail Adan                                                 #
#  Project: TasCLI                                                     #
#  Description: Entry point for TasCLI,                                #
#               controls the flow between the different programs.      #
#               Connects UI with tracker functions                     #
#  Created: October 2025                                               #
#  Notes:                                                              #
#      - Imports all logic from tracker and ui                         #
#      - Ensure projects are saved before exit                         #
# ==================================================================== #

from tracker import *
from interface import run_interface

while True:
    # console.clear()
    # choice = show_home_screen(current_projects)
    run_interface(current_projects)
    save_projects(current_projects)




        




