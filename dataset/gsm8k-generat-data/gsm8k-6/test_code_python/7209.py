def solution():
    # Calculate the price of one candy bar and one cotton candy
    price_candy_bar = 2 * 3  # the price of candy bars is twice the cost of caramel
    price_cotton_candy = (1/2) * (4 * price_candy_bar)  # the cost of cotton candy is half the price of 4 candy bars

    # Calculate the total cost of 6 candy bars, 3 caramel, and 1 cotton candy
    total_cost = 6 * price_candy_bar + 3 * 3 + 1 * price_cotton_candy

    result = total_cost
    return result

print(solution())