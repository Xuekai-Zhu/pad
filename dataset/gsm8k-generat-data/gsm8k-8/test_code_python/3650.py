def solution():
    # Define Martin's budget and the initial price of the TV
    budget = 1000
    initial_price = budget

    # Calculate the discounted price of the TV
    discounted_price = initial_price - 100 - (0.2 * initial_price)

    # Calculate the difference between the discounted price and Martin's budget
    price_difference = budget - discounted_price

    result = price_difference
    return result

print(solution())