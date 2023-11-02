def solution():
    # Calculate the cost of the candy
    cost_reeses = 4 * 9  # 4 bags of Reese's at $9 per bag
    cost_snickers = 3 * 5  # 3 bags of Snickers at $5 per bag
    cost_skittles = 5 * 7  # 5 bags of Skittles at $7 per bag
    total_candy_cost = cost_reeses + cost_snickers + cost_skittles

    # Calculate the total cost of the unicorn piñata and candy
    total_cost = 13 + total_candy_cost
    result = total_cost
    return result

print(solution())