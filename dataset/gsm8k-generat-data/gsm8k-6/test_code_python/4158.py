def solution():
    # Calculate the total number of light bulbs
    total_light_bulbs = 20 * 7

    # Calculate the number of lamps with burnt-out light bulbs
    lamps_with_burnt_out_bulbs = 20 / 4

    # Calculate the total number of burnt-out light bulbs
    total_burnt_out_bulbs = lamps_with_burnt_out_bulbs * 2

    # Calculate the number of working light bulbs
    working_bulbs = total_light_bulbs - total_burnt_out_bulbs
    result = working_bulbs
    return result

print(solution())