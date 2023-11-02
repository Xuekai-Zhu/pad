def solution():
    # Define the original prices of the fruits
    lemon_price_original = 8
    grape_price_original = 7

    # Define the number of lemons and grapes in the basket
    num_lemons = 80
    num_grapes = 140

    # Calculate the new prices of the fruits
    lemon_price_new = lemon_price_original + 4
    grape_price_increase = 0.5 * 4  # half the increase in lemon price
    grape_price_new = grape_price_original + grape_price_increase

    # Calculate the total amount of money collected from selling the fruits at the new prices
    total_money_collected = num_lemons * lemon_price_new + num_grapes * grape_price_new
    result = total_money_collected
    return result

print(solution())