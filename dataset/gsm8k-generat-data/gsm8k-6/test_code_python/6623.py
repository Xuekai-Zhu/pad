def solution():
    # Calculate the combined rate of loading compost
    combined_rate = 75 + 10  # Steven's tractor scoops up 75 pounds per minute, Darrel can scoop up 10 pounds per minute

    # Calculate the time it will take to load 2550 pounds of compost
    time = 2550 / combined_rate
    result = time
    return result

print(solution())