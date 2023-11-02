def solution():
    """Peter has 15 birds. 1/3 are ducks. The rest are chickens and require special feed that costs $2 per bird. How much does it cost to feed the chickens?"""
    total_birds = 15
    ducks = total_birds // 3
    chickens = total_birds - ducks
    chicken_feed_cost = chickens * 2
    result = chicken_feed_cost
    return result

print(solution())