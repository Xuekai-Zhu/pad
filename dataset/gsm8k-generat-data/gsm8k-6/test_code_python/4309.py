def solution():
    # Calculate the total area of the road to be paved
    total_area = 2000 * 20  # length * width

    # Calculate the number of truckloads of asphalt required
    num_truckloads = total_area/800

    # Calculate the cost of the asphalt before tax
    cost_before_tax = num_truckloads * 75

    # Calculate the tax amount
    tax_amount = cost_before_tax * 0.2

    # Calculate the total cost including tax
    total_cost = cost_before_tax + tax_amount

    result = total_cost
    return result

print(solution())