def solution():
    available_money = 50
    cake_price = 20
    bouquet_price = 36
    balloons_price = 5

    # Calculate the total cost of all items
    total_cost = cake_price + bouquet_price + balloons_price

    # Calculate how much more money Michael needs to buy all items
    remaining_money = total_cost - available_money
    result = remaining_money
    return result

print(solution())