def solution():
    """Robie bought 3 bags of chocolates. She gave the 2 bags to her brothers and sisters then bought another 3 bags. How many bags of chocolates were left?"""
    initial_bags = 3
    given_bags = 2
    additional_bags = 3
    total_bags = initial_bags - given_bags + additional_bags
    result = total_bags
    return result

print(solution())