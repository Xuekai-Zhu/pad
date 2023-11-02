def solution():
    """Dany owns a farm, in his farm he has 4 cows and 3 sheep that eat 2 bushels a day. He also has 7 chickens that eat 3 bushels a day. How many bushels should he have to suffice the animals for a day?"""
    cows = 4
    sheep = 3
    chickens = 7
    bushels_per_day = 2 * (cows + sheep) + 3 * chickens
    result = bushels_per_day
    return result

print(solution())