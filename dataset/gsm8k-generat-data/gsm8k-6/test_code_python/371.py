def solution():
    hamburgers_left = 115 - 40  # hamburgers left to cook
    sessions_needed = hamburgers_left // 15  # number of sessions needed
    if hamburgers_left % 15 != 0:  # if there are hamburgers left over after full sessions, add one more session
        sessions_needed += 1
    result = sessions_needed
    return result

print(solution())