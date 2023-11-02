def solution():
    # Calculate the amount of money Jake gave to his friend
    feeding_allowance = 4
    fraction_given = 1/4
    amount_given = fraction_given * feeding_allowance

    # Calculate the number of candies that can be purchased with the given amount of money
    candy_cost = 0.2
    candies = int(amount_given / candy_cost)

    result = candies
    return result

print(solution())