def solution():
    # Define the time it takes for Tobias to swim 100 meters and to take a pause
    swim_time = 5
    pause_time = 5

    # Calculate the number of times Tobias took a pause during his swim
    pause_count = (3 * 60) // (25 + 5)

    # Calculate the total time Tobias spent swimming
    total_swim_time = (3 * 60) - (pause_count * (pause_time + 25))

    # Calculate the distance Tobias swam
    distance_swam = (total_swim_time // swim_time) * 100

    result = distance_swam
    return result

print(solution())