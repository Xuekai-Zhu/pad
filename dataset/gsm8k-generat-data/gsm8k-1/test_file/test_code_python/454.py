def solution():
    """Jennifer's dog has 8 puppies, 3 of which have spots. Brandon's dog has 12 puppies, 4 of which have spots. What percentage of all the puppies have spots?"""
    total_puppies = 8 + 12
    puppies_with_spots = 3 + 4
    percentage_with_spots = (puppies_with_spots / total_puppies) * 100
    result = percentage_with_spots
    return result

print(solution())