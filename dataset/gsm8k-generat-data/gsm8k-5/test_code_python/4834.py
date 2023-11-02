def solution():
    rung_length = 18 / 12  # Convert rung length from inches to feet
    space_between_rungs = 6 / 12  # Convert space between rungs from inches to feet
    total_length = 50  # James needs to climb 50 feet

    # Calculate the number of rungs needed
    num_rungs = (total_length / space_between_rungs) - 1

    # Calculate the total length of wood needed for the rungs
    wood_length = num_rungs * rung_length
    result = wood_length
    return result

print(solution())