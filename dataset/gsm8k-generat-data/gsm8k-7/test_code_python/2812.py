def solution():
    magazine_cost = 3.0
    magazines_bought = 10
    selling_price = 3.5

    # Calculate the total cost of buying all the magazines
    total_cost = magazine_cost * magazines_bought

    # Calculate the total revenue from selling all the magazines
    total_revenue = selling_price * magazines_bought

    # Calculate the profit from selling all the magazines
    total_profit = total_revenue - total_cost
    result = total_profit
    return result

print(solution())