def solution():
    """James has 28 marbles. He puts them into 4 bags. He puts the same number in each bag. He then gives one bag away. How many marbles does James have left?"""
    num_bags = 4
    total_marbles = 28
    marbles_per_bag = total_marbles // num_bags
    remaining_bags = num_bags - 1
    remaining_marbles = marbles_per_bag * remaining_bags
    result = remaining_marbles
    return result

print(solution())