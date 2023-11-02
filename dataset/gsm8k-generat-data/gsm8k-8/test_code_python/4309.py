def solution():
    # Calculate the total area of the road
    road_area = 2000 * 20

    # Calculate the number of truckloads needed
    truckloads = road_area / 800

    # Calculate the cost of the asphalt before tax
    cost_before_tax = truckloads * 75

    # Calculate the amount of sales tax
    sales_tax = 0.2 * cost_before_tax

    # Calculate the total cost with tax
    total_cost = cost_before_tax + sales_tax

    result = total_cost
    return result

print(solution())