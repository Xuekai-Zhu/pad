def solution():
    """Julie had $500. She spent 20% of it on clothes and then 25% of the remaining money on CDs. How much money did Julie have left?"""
    starting_money = 500
    clothes_cost = starting_money * 0.2
    remaining_money = starting_money - clothes_cost
    cd_cost = remaining_money * 0.25
    money_left = remaining_money - cd_cost
    result = money_left
    return result

print(solution())