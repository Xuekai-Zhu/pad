def solution():
    """Carson leans over the railing at the zoo to get the perfect selfie and falls into the combined wombat and rhea enclosure. There are 9 wombats and 3 rheas. If each wombat claws him 4 times and each rhea claws him once, how many times does he get clawed?"""
    wombat_claws = 4
    rhea_claws = 1
    total_wombat_claws = wombat_claws * 9
    total_rhea_claws = rhea_claws * 3
    total_claws = total_wombat_claws + total_rhea_claws
    result = total_claws
    return result

print(solution())