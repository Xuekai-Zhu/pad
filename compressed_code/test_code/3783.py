def solution():
    
    total_birds = 15
    ducks = total_birds // 3
    chickens = total_birds - ducks
    chicken_feed_cost = chickens * 2
    result = chicken_feed_cost
    return result

print(solution())