def solution():
    """Jason has a moray eel that eats 20 guppies a day and 5 betta fish who each eat 7 guppies a day. How many guppies per day does she need to buy?"""
    guppies_per_betta = 7
    bettas = 5
    moray_eel = 20
    total_guppies = (guppies_per_betta * bettas) + moray_eel
    result = total_guppies
    return result

print(solution())