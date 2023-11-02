def solution():
    # Define the volume of the water bottle in ml
    bottle_volume = 2000

    # Define the volume of each sip in ml
    sip_volume = 40

    # Calculate the number of sips in the bottle
    number_of_sips = bottle_volume / sip_volume

    # Calculate the time it takes to consume all the sips in minutes
    time_in_minutes = number_of_sips * 5

    result = time_in_minutes
    return result

print(solution())