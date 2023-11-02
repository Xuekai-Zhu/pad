def solution():
    """Mark is buying asphalt to pave a new section of road. The road will be 2000 feet long and 20 feet wide. Each truckload of asphalt will cover 800 square feet of road. If each truckload costs $75, and there's a 20% sales tax, how much will Mark need to pay for asphalt?"""
    # Calculate the total area of the road to be paved
    area = 2000 * 20

    # Calculate the number of truckloads needed
    num_truckloads = area / 800

    # Calculate the cost of the asphalt before tax
    cost_before_tax = num_truckloads * 75

    # Calculate the sales tax
    sales_tax = 0.2 * cost_before_tax

    # Calculate the total cost including tax
    total_cost = cost_before_tax + sales_tax

    # Display the total cost
    result = total_cost
    return result

print(solution())