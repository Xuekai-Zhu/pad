def solution():
    # Define the compost weight and scoop rates
    compost_weight = 2550
    tractor_rate = 75
    shovel_rate = 10

    # Calculate the combined scoop rate
    combined_rate = tractor_rate + shovel_rate

    # Calculate the time it would take to load the compost with both scoops working
    time = compost_weight / combined_rate
    result = time
    return result

print(solution())