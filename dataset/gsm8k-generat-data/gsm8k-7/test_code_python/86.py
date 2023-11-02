def solution():
    starting_cash = 2.0
    ending_cash = 0.5
    soda_price = 0.25

    # Calculate the amount of cash used to buy soda
    cash_for_soda = starting_cash - ending_cash

    # Calculate the number of ounces of soda purchased
    num_ounces = cash_for_soda / soda_price
    result = num_ounces
    return result

print(solution())