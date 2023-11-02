def solution():
    """For the family reunion, Peter is buying 16 pounds of bone-in chicken and half that amount in hamburgers. He's going to buy 2 more pounds of hot dogs than hamburgers. He's also going to buy several sides that will weigh half the amount of hot dogs. How many pounds of food will he buy?"""
    chicken = 16
    hamburgers = chicken / 2
    hotdogs = hamburgers + 2
    sides = hotdogs / 2
    total_weight = chicken + hamburgers + hotdogs + sides
    result = total_weight
    return result

print(solution())