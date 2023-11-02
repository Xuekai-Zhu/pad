def solution():
    tractor_rate = 75   # pounds per minute
    darrel_rate = 10    # pounds per minute
    target_weight = 2550    # pounds

    # Calculate the combined rate of Steven and Darrell
    combined_rate = tractor_rate + darrel_rate

    # Calculate the time it would take for the two of them working together to load up the compost
    time = target_weight / combined_rate
    result = time
    return result

print(solution())