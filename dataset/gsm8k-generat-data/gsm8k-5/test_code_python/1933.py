def solution():
    filling_cost = 120  # Cost of one filling
    cleaning_cost = 70  # Cost of one cleaning
    total_bill = 5 * filling_cost + cleaning_cost + tooth_extraction_cost  # Wendy's total bill
    tooth_extraction_cost = total_bill - (5 * filling_cost + cleaning_cost)  # Cost of tooth extraction

    result = tooth_extraction_cost
    return result

print(solution())