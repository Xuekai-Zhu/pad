def solution():
    rate_steven = 75  # Steven's tractor can scoop up 75 pounds of compost per minute
    rate_darrel = 10  # Darrel can scoop up 10 pounds of compost per minute
    total_compost = 2550  # The truck needs to be loaded with 2550 pounds of compost

    # Calculate the combined rate of Steven and Darrel
    combined_rate = rate_steven + rate_darrel

    # Calculate the time needed for both of them to load up the truck
    time_needed = total_compost / combined_rate
    result = time_needed
    return result

print(solution())