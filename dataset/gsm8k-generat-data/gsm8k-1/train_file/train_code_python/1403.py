def solution():
    """Carson leans over the railing at the zoo to get the perfect selfie and falls into the combined wombat and rhea enclosure. There are 9 wombats and 3 rheas. If each wombat claws him 4 times and each rhea claws him once, how many times does he get clawed?"""
    wombats = 9
    wombat_claws = 4
    rheas = 3
    rhea_claws = 1
    total_claws = wombats * wombat_claws + rheas * rhea_claws
    result = total_claws
    return result

print(solution())