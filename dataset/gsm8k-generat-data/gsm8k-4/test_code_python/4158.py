def solution():
    """Reyna had 20 lamps with seven light bulbs in each lamp. If 1/4 of them have 2 burnt-out light bulbs each, how many light bulbs are working?"""
    # Define the initial number of lamps and bulbs per lamp
    num_lamps = 20
    num_bulbs = 7

    # Calculate the total number of bulbs
    total_bulbs = num_lamps * num_bulbs

    # Calculate the number of lamps with burnt-out bulbs
    num_faulty_lamps = num_lamps // 4

    # Calculate the total number of burnt-out bulbs
    num_faulty_bulbs = num_faulty_lamps * 2

    # Calculate the number of working bulbs
    num_working_bulbs = total_bulbs - num_faulty_bulbs

    # Return the result
    result = num_working_bulbs
    return result

print(solution())