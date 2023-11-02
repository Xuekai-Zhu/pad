def solution():
    ounces_per_hamburger = 4  # Each hamburger is 4 ounces
    ounces_to_beat = 84  # Last year's winner ate 84 ounces
    hamburgers_to_beat = ounces_to_beat / ounces_per_hamburger  # Calculate the number of hamburgers to beat

    # Round up to the nearest whole number of hamburgers
    hamburgers_to_beat = int(hamburgers_to_beat) if hamburgers_to_beat.is_integer() else int(hamburgers_to_beat) + 1

    result = hamburgers_to_beat
    return result

print(solution())