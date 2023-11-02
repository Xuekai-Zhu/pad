def solution():
    num_packs = 8
    pack_price = 4
    num_bags_per_pack = 5
    sale_price = 8

    # Calculate the total cost of all canvas bags
    total_cost = num_packs * pack_price

    # Calculate the total revenue from selling all canvas bags
    total_revenue = num_bags_per_pack * sale_price

    # Calculate the profit
    profit = total_revenue - total_cost
    result = profit
    return result

print(solution())