def solution():
    hamburgers_per_session = 15
    total_hamburgers = 115
    hamburgers_cooked = 40

    hamburgers_left = total_hamburgers - hamburgers_cooked
    sessions_needed = hamburgers_left / hamburgers_per_session

    # Round up the number of sessions
    sessions_needed = math.ceil(sessions_needed)

    result = sessions_needed
    return result

print(solution())