def solution():
    """Craig has 2 twenty dollar bills. He buys six squirt guns for $2 each. He also buys 3 packs of water balloons for $3 each. How much money does he have left?"""
    starting_money = 2 * 20
    squirt_gun_cost = 6 * 2
    water_balloon_cost = 3 * 3
    total_cost = squirt_gun_cost + water_balloon_cost
    remaining_money = starting_money - total_cost
    result = remaining_money
    return result

print(solution())