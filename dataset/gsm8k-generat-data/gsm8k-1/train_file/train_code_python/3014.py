def solution():
    """Sam has 19 dimes and 6 quarters. She buys 4 candy bars for 3 dimes each and 1 lollipop for 1 quarter. How much money, in cents, does she have left?"""
    num_dimes = 19
    num_quarters = 6
    candy_bar_price = 3 * 10 # convert to cents
    lollipop_price = 25 # cents
    total_cost = (4 * candy_bar_price) + lollipop_price
    total_paid = (num_dimes * 10) + (num_quarters * 25)
    remaining_money = total_paid - total_cost
    result = remaining_money
    return result

print(solution())