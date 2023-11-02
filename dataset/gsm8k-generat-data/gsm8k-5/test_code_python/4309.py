def solution():
    road_length = 2000  # The road is 2000 feet long
    road_width = 20  # The road is 20 feet wide
    area_per_truck = 800  # Each truckload of asphalt covers 800 square feet of road
    cost_per_truck = 75  # Each truckload of asphalt costs $75
    sales_tax = 0.2  # The sales tax is 20%

    # Calculate the total area of the road to be paved
    total_area = road_length * road_width

    # Calculate the total number of truckloads of asphalt needed
    total_truckloads = total_area / area_per_truck

    # Calculate the total cost of the asphalt without sales tax
    cost_before_tax = total_truckloads * cost_per_truck

    # Calculate the sales tax
    tax_amount = cost_before_tax * sales_tax

    # Calculate the total cost of the asphalt including sales tax
    total_cost = cost_before_tax + tax_amount
    result = total_cost
    return result

print(solution())