def solution():
    advertising_cost = 1000
    num_customers = 100
    conversion_rate = 0.8
    item_price = 25

    # Calculate the number of customers who bought something
    num_buyers = num_customers * conversion_rate

    # Calculate the total revenue from those who bought something
    total_revenue = num_buyers * item_price

    # Calculate the profit from the advertising
    profit = total_revenue - advertising_cost
    result = profit
    return result

print(solution())