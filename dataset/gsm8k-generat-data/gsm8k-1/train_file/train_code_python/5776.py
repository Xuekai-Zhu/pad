def solution():
    """For the family reunion, Peter is buying 16 pounds of bone-in chicken and half that amount in hamburgers. He's going to buy 2 more pounds of hot dogs than hamburgers. He's also going to buy several sides that will weigh half the amount of hot dogs. How many pounds of food will he buy?"""
    chicken_weight = 16
    hamburger_weight = chicken_weight / 2
    hotdog_weight = hamburger_weight + 2
    side_weight = hotdog_weight / 2
    total_weight = chicken_weight + hamburger_weight + hotdog_weight + side_weight
    result = total_weight
    return result

print(solution())