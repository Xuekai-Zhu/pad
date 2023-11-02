def solution():
    """John bakes 12 coconut macaroons, each weighing 5 ounces. He then packs an equal number of the macaroons in 4 different brown bags, ready for delivery. When he briefly leaves the kitchen to pick the phone, his little brother Steve eats the entire contents of one of the brown bags. What is the total weight, in ounces, of the remaining coconut macaroons?"""
    macaroons_per_bag = 12/4
    macaroon_weight = 5
    eaten_macaroons = macaroons_per_bag
    remaining_macaroons = 12 - macaroons_per_bag
    total_weight = remaining_macaroons * macaroon_weight
    result = total_weight
    return result

print(solution())