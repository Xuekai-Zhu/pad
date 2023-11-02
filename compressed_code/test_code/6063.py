def solution():
    
    hamburgers_per_session = 15
    total_hamburgers = 115
    hamburgers_already_cooked = 40
    hamburgers_left = total_hamburgers - hamburgers_already_cooked
    sessions_needed = hamburgers_left // hamburgers_per_session + (hamburgers_left % hamburgers_per_session > 0)
    result = sessions_needed
    return result

print(solution())