def solution():
    necklaces_sold = 4  # Linda sold 4 necklaces
    total_sales = 80  # Linda's total sales were $80
    cost_per_necklace = 12  # Each necklace costs $12

    # Calculate the revenue from selling necklaces
    revenue_necklaces = necklaces_sold * cost_per_necklace

    # Calculate the revenue from selling rings
    revenue_rings = total_sales - revenue_necklaces

    # Calculate the cost per ring
    cost_per_ring = revenue_rings / 8
    result = cost_per_ring
    return result

print(solution())