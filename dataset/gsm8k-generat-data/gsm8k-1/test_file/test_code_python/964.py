def solution():
    """Andy works in the pro shop of a tennis resort. He has 12 racquets that need restringing. 3 of them are to be strung with synthetic gut, 5 of them will be strung with polyester string, and 4 of them will be strung with a hybrid set (half synthetic gut, half polyester string). How long will it take Andy to string all of those racquets if it takes him an average of 15 minutes for him to string with synthetic gut, 22 minutes to string with polyester string, and 18 minutes for hybrid sets?"""
    synthetic_gut_racquets = 3
    polyester_racquets = 5
    hybrid_racquets = 4
    synthetic_gut_time = 15
    polyester_time = 22
    hybrid_time = 18
    total_time = (synthetic_gut_racquets * synthetic_gut_time) + (polyester_racquets * polyester_time) + (hybrid_racquets * hybrid_time)
    result = total_time
    return result

print(solution())