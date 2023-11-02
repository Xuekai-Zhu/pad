def solution():
    char_per_necklace = 10
    cost_per_char = 15
    price_per_necklace = 200
    num_necklaces_sold = 30

    # Calculate the total cost of making all necklaces
    cost_of_charms = char_per_necklace * cost_per_char
    total_cost = cost_of_charms * num_necklaces_sold

    # Calculate the total revenue from selling all necklaces
    total_revenue = price_per_necklace * num_necklaces_sold

    # Calculate the profit
    profit = total_revenue - total_cost
    result = profit
    return result

print(solution())