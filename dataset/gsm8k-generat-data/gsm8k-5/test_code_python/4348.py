def solution():
    cost_per_duck = 10  # John pays $10 for each duck
    num_ducks = 30  # John buys 30 ducks
    total_cost = cost_per_duck * num_ducks  # John's total cost is the cost per duck multiplied by the number of ducks

    duck_weight = 4  # Each duck weighs 4 pounds
    selling_price_per_pound = 5  # John sells ducks for $5 per pound
    total_weight = num_ducks * duck_weight  # John's total weight is the number of ducks multiplied by their weight

    # Calculate John's revenue from selling the ducks
    revenue = total_weight * selling_price_per_pound
    profit = revenue - total_cost  # Profit is revenue minus cost
    result = profit
    return result

print(solution())