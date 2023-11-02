def solution():
    # Calculate the total number of rungs James needs
    total_rungs = (50*12) / 6  # convert 50 feet to inches and divide by the distance between rungs (inches)

    # Calculate the total length of wood needed for the rungs
    length_wood = total_rungs * 18  # each rung is 18 inches long

    # Convert length to feet
    length_feet = length_wood / 12

    result = length_feet
    return result

print(solution())