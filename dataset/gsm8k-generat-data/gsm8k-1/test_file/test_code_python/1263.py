def solution():
    """A farm has 10 2-legged animals and 15 4-legged animals. If all animals are healthy, how many pairs of animal legs in total are on the farm?"""
    two_legged_animals = 10
    four_legged_animals = 15
    total_legs = (two_legged_animals * 2) + (four_legged_animals * 4)
    pairs_of_legs = total_legs // 2
    result = pairs_of_legs
    return result

print(solution())