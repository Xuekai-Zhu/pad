def solution():
    # Define the cost of a filling
    filling_cost = 120

    # Calculate the total cost of Wendy's bill
    total_cost = filling_cost * 5

    # Subtract the cost of the cleaning and two fillings to find the cost of the extraction
    extraction_cost = total_cost - (70 + 2 * filling_cost)
    result = extraction_cost
    return result

print(solution())