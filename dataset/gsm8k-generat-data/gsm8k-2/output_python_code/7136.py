def solution():
    """John bakes 12 coconut macaroons, each weighing 5 ounces. He then packs an equal number of the macaroons in 4 different brown bags, ready for delivery. When he briefly leaves the kitchen to pick the phone, his little brother Steve eats the entire contents of one of the brown bags. What is the total weight, in ounces, of the remaining coconut macaroons?"""
    total_macaroons = 12
    macaroon_weight = 5
    macaroons_per_bag = total_macaroons // 4
    remaining_macaroons = total_macaroons - macaroons_per_bag
    remaining_weight = remaining_macaroons * macaroon_weight
    result = remaining_weight
    return result

print(solution())