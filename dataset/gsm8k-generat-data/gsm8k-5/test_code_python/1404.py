def solution():
    numb_wombats = 9  # There are 9 wombats in the enclosure
    numb_rheas = 3  # There are 3 rheas in the enclosure
    claw_wombat = 4  # Each wombat claws Carson 4 times
    claw_rhea = 1  # Each rhea claws Carson once

    # Calculate the total number of times Carson gets clawed
    total_claws = (numb_wombats * claw_wombat) + (numb_rheas * claw_rhea)
    result = total_claws
    return result

print(solution())