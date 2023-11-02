def solution():
    tea_price = 10  # The price of tea is given as $10
    cheese_price = tea_price / 2  # The price of cheese is half the price of tea
    butter_price = 0.8 * (2 * cheese_price)  # The price of butter is 80% the price of cheese
    bread_price = 2 * butter_price / 3  # The price of bread is 2/3 the price of butter

    # Calculate the total cost of Ursula's purchases
    total_cost = tea_price + cheese_price + butter_price + bread_price
    result = total_cost
    return result

print(solution())