def solution():
    # Define the base cost and the total cost of Chris's bill
    base_cost = 45
    total_cost = 65

    # Calculate the amount charged for the additional GB usage
    additional_cost = total_cost - base_cost
    additional_gb = additional_cost / 0.25
    result = additional_gb
    return result

print(solution())