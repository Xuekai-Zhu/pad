def solution():
    # Calculate the total time spent in mazes so far
    total_time_spent = 45 + 4*50

    # Calculate how much time Frank can spend in the current maze
    max_time = 60 - (total_time_spent / 5)

    result = max_time
    return result

print(solution())