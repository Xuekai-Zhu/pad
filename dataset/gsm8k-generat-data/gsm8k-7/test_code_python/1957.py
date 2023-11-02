def solution():
    num_newspapers = 500
    newspaper_price = 2.0
    sell_percentage = 0.8
    buy_discount = 0.75

    # Calculate the total revenue from selling newspapers
    total_revenue = num_newspapers * newspaper_price * sell_percentage

    # Calculate the total cost of buying newspapers
    total_cost = total_revenue * (1 - buy_discount)

    # Calculate the profit
    profit = total_revenue - total_cost
    result = profit
    return result

print(solution())