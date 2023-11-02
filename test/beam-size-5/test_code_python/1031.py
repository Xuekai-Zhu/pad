def solution():
    driveway_width = 24  # Richard's driveway is 24 feet wide
    soda_per_bottle = 1/3  # Richard wants to put a bottle of soda every 3 feet of the driveway
    seconds_per_bottle = 5  # It will take Richard 5 seconds to go from one soda bottle to the next

    # Calculate the total time it will take Richard to set off all the soda bottles
    total_time = (driveway_width * seconds_per_bottle) + seconds_per_bottle
    result = total_time
    return result

print(solution())