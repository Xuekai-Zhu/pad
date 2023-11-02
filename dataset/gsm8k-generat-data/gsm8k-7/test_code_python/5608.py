def solution():
    selling_price = 3
    total_profit = 105
    num_watermelons = 18

    # Calculate the total revenue from selling all watermelons
    total_revenue = num_watermelons * selling_price

    # Calculate the cost of all watermelons
    total_cost = total_revenue - total_profit

    # Calculate the cost of one watermelon
    cost_per_watermelon = total_cost / num_watermelons

    # Calculate the number of watermelons Carl started with
    starting_watermelons = total_revenue / (selling_price + cost_per_watermelon)
    result = starting_watermelons
    return result

print(solution())