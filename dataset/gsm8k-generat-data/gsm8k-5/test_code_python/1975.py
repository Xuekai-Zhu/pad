def solution():
    # Calculate the amount of money in the account after 1 year with 20% interest
    initial_amount = 1000
    interest_1 = initial_amount * 0.2
    total_amount_1 = initial_amount + interest_1

    # Calculate the amount of money Tony takes out to buy a new TV
    amount_for_TV = total_amount_1 / 2

    # Calculate the amount of money left in the account after buying the TV
    remaining_amount = total_amount_1 - amount_for_TV

    # Calculate the amount of money in the account after 1 more year with 15% interest
    interest_2 = remaining_amount * 0.15
    total_amount_2 = remaining_amount + interest_2

    result = total_amount_2
    return result

print(solution())