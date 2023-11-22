def solution():
    
    # Define the distance to swim
    distance = 20

    # Calculate the time it takes to swim the lake
    swim_time = distance * 0.6 / 2

    # Calculate the time it takes to finish the lake
    finish_time = distance / 2 / 2

    # Calculate the total time it takes to get across the lake
    total_time = swim_time + finish_time

    # Display the total time
    result = total_time
    return result

print(solution())