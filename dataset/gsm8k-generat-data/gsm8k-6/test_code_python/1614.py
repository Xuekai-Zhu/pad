def solution():
    # Calculate the time it takes to travel to Boston and back using route A
    time_A = 5 + 5  # total time is twice the time it takes to get to Boston
    # Calculate the time it takes to travel to Boston and back using route B
    time_B = 2 + 2  # total time is twice the time it takes to get to Boston
    # Calculate the time saved by taking route B
    time_saved = time_A - time_B
    result = time_saved
    return result

print(solution())