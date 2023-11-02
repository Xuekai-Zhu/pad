def solution():
    # Calculate the time taken by Matt to reach 220 steps
    time_matt = 220 / 20  # 20 steps per minute

    # Calculate the number of steps Tom goes up in this time
    steps_tom = (20 + 5) * time_matt  # 5 steps per minute more than Matt

    result = steps_tom
    return result

print(solution())