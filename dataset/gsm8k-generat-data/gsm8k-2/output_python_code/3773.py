def solution():
    """Oliver has two bags of vegetables. Each bag weighs 1/6 as much as James’s bag, which weighs 18kg. What is the combined weight of both Oliver’s bags?"""
    james_bag_weight = 18
    oliver_bag_weight = james_bag_weight / 6
    total_oliver_bag_weight = oliver_bag_weight * 2
    result = total_oliver_bag_weight
    return result

print(solution())