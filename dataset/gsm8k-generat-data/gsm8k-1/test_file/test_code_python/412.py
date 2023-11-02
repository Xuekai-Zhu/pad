def solution():
    """A herd consists of camels and dromedaries. There are 180 heads and 304 bumps. How many dromedaries are there if camels have two humps each and dromedaries have one hump each?"""
    total_animals = 180
    total_humps = 304
    camels_humps = 2
    dromedaries_humps = 1
    dromedaries = (total_humps - (total_animals * camels_humps)) / (dromedaries_humps - camels_humps)
    result = dromedaries
    return result

print(solution())