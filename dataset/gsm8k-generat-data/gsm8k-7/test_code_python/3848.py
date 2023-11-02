def solution():
    num_coins = 20
    original_cost = 15
    increase = 2/3

    # Calculate the new value of each coin after the increase
    new_value = original_cost * (1 + increase)

    # Calculate the total value of his investment
    total_value = num_coins * new_value

    # Calculate the amount he needs to sell in order to recoup his original investment
    amount_to_sell = original_cost * num_coins / new_value
    result = amount_to_sell
    return result

print(solution())