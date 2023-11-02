def solution():
    """Sam has 19 dimes and 6 quarters. She buys 4 candy bars for 3 dimes each and 1 lollipop for 1 quarter. How much money, in cents, does she have left?"""
    candy_bar_cost = 3 * 10  # 1 dime = 10 cents
    lollipop_cost = 25  # 1 quarter = 25 cents
    total_cost = 4 * candy_bar_cost + lollipop_cost
    total_money = 19 * 10 + 6 * 25  # in cents
    money_left = total_money - total_cost
    result = money_left
    return result

print(solution())