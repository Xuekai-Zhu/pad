def solution():
    # Cost of 6 pineapples
    cost_of_pineapples = 6 * 3  # $3 per pineapple

    # Total number of pineapple rings
    total_rings = 6 * 12  # 12 rings per pineapple, 6 pineapples

    # Total revenue from selling pineapple rings
    total_revenue = (total_rings / 4) * 5  # $5 for 4 pineapple rings

    # Profit
    profit = total_revenue - cost_of_pineapples
    result = profit
    return result

print(solution())