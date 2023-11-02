def solution():
    # Calculate the number of potato bundles and the revenue from selling them
    num_potato_bundles = 250 // 25  # 25 potatoes per bundle
    revenue_potatoes = num_potato_bundles * 1.90

    # Calculate the number of carrot bundles and the revenue from selling them
    num_carrot_bundles = 320 // 20  # 20 carrots per bundle
    revenue_carrots = num_carrot_bundles * 2

    # Calculate the total revenue from selling all the harvested crops
    total_revenue = revenue_potatoes + revenue_carrots
    result = total_revenue
    return result

print(solution())