def solution():
    num_kids = 4
    num_whiteboards = 3
    time = 20
    
    # Calculate the rate of washing of a single kid
    rate = num_whiteboards / (num_kids * time)

    # Calculate the time needed for a single kid to wash six whiteboards
    time_needed = 6 / rate
    result = time_needed
    return result

print(solution())