def solution():
    """Jason has a moray eel that eats 20 guppies a day and 5 betta fish who each eat 7 guppies a day. How many guppies per day does she need to buy?"""
    eel_guppies_per_day = 20
    betta_fish = 5
    betta_guppies_per_day = betta_fish * 7
    total_guppies_per_day = eel_guppies_per_day + betta_guppies_per_day
    result = total_guppies_per_day
    return result

print(solution())