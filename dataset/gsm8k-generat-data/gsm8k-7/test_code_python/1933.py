def solution():
    cleaning_cost = 70
    filling_cost = 120
    bill_multiplier = 5

    # Calculate the cost of a tooth extraction
    extraction_cost = (bill_multiplier * filling_cost) - (2 * filling_cost) - cleaning_cost

    result = extraction_cost
    return result

print(solution())