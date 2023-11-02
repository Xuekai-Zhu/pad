def solution():
    capacity_per_crate = 20  # in kilograms
    num_crates = 3
    total_cost = 330
    selling_price_per_kg = 6
    rotten_tomatoes = 3  # in kilograms

    # Calculate the total weight of all the tomatoes
    total_weight = capacity_per_crate * num_crates

    # Subtract the weight of the rotten tomatoes
    total_weight -= rotten_tomatoes

    # Calculate the total revenue from selling all non-rotten tomatoes
    total_revenue = total_weight * selling_price_per_kg

    # Calculate Tommy's profit by subtracting the total cost from the total revenue
    profit = total_revenue - total_cost
    result = profit
    return result

print(solution())