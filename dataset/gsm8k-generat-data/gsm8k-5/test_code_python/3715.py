def solution():
    # Calculate the cost of buying all the boxes
    cost_of_boxes = 12 * 10 * 30  # 12 boxes, $10 per box, 30 pens per box

    # Calculate the revenue from selling the packages of 6 highlighters
    revenue_from_packages = 5 * (10/6) * 3  # 5 boxes, rearranged into 50 packages of 6, sold at $3 per package

    # Calculate the revenue from selling the remaining highlighters separately
    remaining_pens = 7 * 30  # 7 boxes left, with 30 pens each
    revenue_from_remaining = (remaining_pens / 3) * 2  # Sold at $2 for 3 pens

    # Calculate the total profit
    total_profit = revenue_from_packages + revenue_from_remaining - cost_of_boxes
    result = total_profit
    return result

print(solution())