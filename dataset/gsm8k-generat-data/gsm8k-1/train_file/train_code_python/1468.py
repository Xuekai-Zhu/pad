def solution():
    """James has 28 marbles. He puts them into 4 bags. He puts the same number in each bag. He then gives one bag away. How many marbles does James have left?"""
    total_marbles = 28
    num_bags = 4
    marbles_per_bag = total_marbles / num_bags
    marbles_left = total_marbles - marbles_per_bag
    result = marbles_left
    return result

print(solution())