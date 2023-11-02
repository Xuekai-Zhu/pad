def solution():
    buy_price = 0.8
    sell_price = 1.0
    num_bought = 50
    num_sold = 48

    # Calculate the total cost of buying all candy bars
    total_cost = buy_price * num_bought

    # Calculate the total sales from selling all candy bars
    total_sales = sell_price * num_sold

    # Calculate the profit in cents
    profit = (total_sales - total_cost) * 100
    result = int(profit)
    return result

print(solution())