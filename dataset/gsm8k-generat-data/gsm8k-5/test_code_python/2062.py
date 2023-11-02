def solution():
    total_time = 120  # Joan has 2 hours, or 120 minutes, for music practice
    time_spent = 30 + 25 + 38  # Joan has already spent this amount of time on other tasks
    time_left = total_time - time_spent  # Joan has this much time left for the finger exerciser
    result = time_left
    return result

print(solution())