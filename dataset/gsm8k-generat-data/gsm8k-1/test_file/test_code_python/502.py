def solution():
    """Mario needs to buy snowshoes for his 6 sled dogs. Assuming his dogs each has four legs and each pair of snowshoes costs $12.00, how much will it cost him to buy snowshoes for all of his dogs?"""
    dogs = 6
    legs_per_dog = 4
    total_legs = dogs * legs_per_dog
    pairs_of_shoes = total_legs / 2
    cost_per_pair = 12.00
    total_cost = pairs_of_shoes * cost_per_pair
    result = total_cost
    return result

print(solution())