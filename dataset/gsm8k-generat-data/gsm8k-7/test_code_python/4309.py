def solution():
    road_length = 2000
    road_width = 20
    coverage_per_truckload = 800
    cost_per_truckload = 75
    sales_tax_rate = 0.2

    # Calculate the total area of the road to be paved
    total_area = road_length * road_width

    # Calculate the total number of truckloads needed
    total_truckloads = total_area / coverage_per_truckload

    # Calculate the total cost of all truckloads before sales tax
    cost_before_tax = total_truckloads * cost_per_truckload

    # Calculate the sales tax to be added
    sales_tax = cost_before_tax * sales_tax_rate

    # Calculate the total cost including sales tax
    total_cost = cost_before_tax + sales_tax
    result = total_cost
    return result

print(solution())