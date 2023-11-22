def solution():
    
    # Define the width of the driveway and the number of bottles needed
    driveway_width = 24
    bottles_needed = driveway_width // 3

    # Calculate the time it takes to go from one bottle to the next bottle
    bottle_time = 5

    # Calculate the total time to go from one bottle to the next bottle
    bottle_total_time = bottles_needed * bottle_time

    # Calculate the total time to set off all the soda
    total_time = bottle_total_time + 5

    # Display the total time
    result = total_time
    return result

print(solution())