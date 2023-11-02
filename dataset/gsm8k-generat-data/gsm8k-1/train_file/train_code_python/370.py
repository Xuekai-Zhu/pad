def solution():
    """Ronald can grill 15 hamburgers per session on his new grill. He needs to cook 115 hamburgers in total for tonight's party. He has already cooked 40 hamburgers. How many more sessions will it take Ronald to finish cooking all 115 hamburgers?"""
    hamburgers_per_session = 15
    total_hamburgers = 115
    hamburgers_already_cooked = 40
    hamburgers_left = total_hamburgers - hamburgers_already_cooked
    sessions_needed = hamburgers_left // hamburgers_per_session + (hamburgers_left % hamburgers_per_session > 0)
    result = sessions_needed
    return result

print(solution())