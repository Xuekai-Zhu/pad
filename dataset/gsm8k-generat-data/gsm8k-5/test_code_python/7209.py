def solution():
    price_caramel = 3  # The price of 1 caramel is $3
    price_candy_bar = 2 * price_caramel  # The price of 1 candy bar is twice the cost of 1 caramel
    price_cotton_candy = price_candy_bar / 2  # The price of 1 cotton candy is half the price of 4 candy bars

    # Calculate the total cost of 6 candy bars
    cost_candy_bars = 6 * price_candy_bar

    # Calculate the total cost of 3 caramel
    cost_caramel = 3 * price_caramel

    # Calculate the total cost of 1 cotton candy
    cost_cotton_candy = price_cotton_candy

    # Calculate the total cost
    total_cost = cost_candy_bars + cost_caramel + cost_cotton_candy
    result = total_cost
    return result

print(solution())