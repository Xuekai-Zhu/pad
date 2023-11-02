def solution():
    total_lamps = 20  # Reyna had 20 lamps
    light_bulbs_per_lamp = 7  # Each lamp has 7 light bulbs
    total_light_bulbs = total_lamps * light_bulbs_per_lamp  # Total number of light bulbs

    # Calculate the number of lamps with 2 burnt-out light bulbs
    burnt_out_lamps = total_lamps / 4
    burnt_out_light_bulbs = burnt_out_lamps * 2

    # Calculate the number of working light bulbs
    working_light_bulbs = total_light_bulbs - burnt_out_light_bulbs
    result = working_light_bulbs
    return result

print(solution())