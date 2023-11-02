def solution():
    # Calculate the total cost of making the pumpkin pies and the cherry pies
    total_cost = 10*3 + 12*5 

    # Calculate the total revenue needed to make a profit of $20
    total_revenue = total_cost + 20

    # Calculate the price to sell each pie
    price_per_pie = total_revenue / (10+12)

    result = price_per_pie
    return result

print(solution())