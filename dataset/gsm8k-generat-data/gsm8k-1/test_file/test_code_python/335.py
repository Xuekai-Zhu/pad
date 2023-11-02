def solution():
    """Farmer Brown has 60 animals on his farm, all either chickens or cows. He has twice as many chickens as cows. How many legs do the animals have, all together?"""
    total_animals = 60
    ratio_chickens_to_cows = 2
    num_cows = total_animals / (ratio_chickens_to_cows + 1)
    num_chickens = total_animals - num_cows
    num_legs_cows = num_cows * 4
    num_legs_chickens = num_chickens * 2
    total_legs = num_legs_cows + num_legs_chickens
    result = total_legs
    
    return result

print(solution())