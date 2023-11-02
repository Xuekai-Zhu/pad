def solution():
    """Mark is buying asphalt to pave a new section of road. The road will be 2000 feet long and 20 feet wide. Each truckload of asphalt will cover 800 square feet of road. If each truckload costs $75, and there's a 20% sales tax, how much will Mark need to pay for asphalt?"""
    # Define the size of the road and the coverage of each truckload of asphalt
    road_length = 2000
    road_width = 20
    asphalt_coverage = 800

    # Calculate the total area of the road
    road_area = road_length * road_width

    # Calculate the total number of truckloads required
    total_truckloads = road_area / asphalt_coverage

    # Calculate the cost of the asphalt before tax
    cost_before_tax = total_truckloads * 75

    # Calculate the sales tax
    sales_tax = 0.2 * cost_before_tax

    # Calculate the total cost including tax
    total_cost = cost_before_tax + sales_tax

    result = total_cost
    return result

print(solution())