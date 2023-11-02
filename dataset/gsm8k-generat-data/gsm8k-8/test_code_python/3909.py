def solution():
    # Calculate the total number of acts
    total_acts = 3 * 5

    # Calculate the total number of wigs used
    total_wigs = total_acts * 2

    # Calculate the total cost of all the wigs
    total_cost = total_wigs * 5

    # Calculate the money earned from selling the wigs from one play
    wig_sell_price = 4 * total_wigs / 3

    # Calculate the final spent money
    spent_money = total_cost - wig_sell_price
    result = spent_money
    return result

print(solution())