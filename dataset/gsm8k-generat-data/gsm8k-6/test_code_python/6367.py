def solution():
    # Calculate the cost and revenue of the sale
    cost = 90  # Bert bought the barrel for $90
    revenue = cost + 10  # Bert sells the product for $10 more

    # Calculate the amount of tax Bert has to pay
    tax = 0.1 * revenue

    # Calculate the profit Bert made on the sale
    profit = revenue - cost - tax
    result = profit
    return result

print(solution())