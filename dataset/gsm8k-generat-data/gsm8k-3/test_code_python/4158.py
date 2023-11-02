def solution():
    """Reyna had 20 lamps with seven light bulbs in each lamp. If 1/4 of them have 2 burnt-out light bulbs each, how many light bulbs are working?"""
    # Define the number of lamps and light bulbs per lamp
    NUM_LAMPS = 20
    NUM_LIGHT_BULBS_PER_LAMP = 7

    # Calculate the total number of light bulbs
    total_light_bulbs = NUM_LAMPS * NUM_LIGHT_BULBS_PER_LAMP

    # Calculate the number of lamps with 2 burnt-out light bulbs
    num_burnt_out = NUM_LAMPS // 4
    num_lamps_with_burnt_out = num_burnt_out * 2

    # Calculate the number of working light bulbs
    num_working_light_bulbs = total_light_bulbs - num_lamps_with_burnt_out * 2

    # Display the number of working light bulbs
    result = num_working_light_bulbs
    return result

print(solution())