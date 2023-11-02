def solution():
    """There are 27 unicorns left in the world. One third of them are in the Scottish Highlands. Two thirds of the Scottish unicorns are female. How many female Scottish unicorns are there?"""
    total_unicorns = 27
    scottish_unicorns = total_unicorns / 3
    female_scottish_unicorns = scottish_unicorns * (2/3)
    result = female_scottish_unicorns
    return result

print(solution())