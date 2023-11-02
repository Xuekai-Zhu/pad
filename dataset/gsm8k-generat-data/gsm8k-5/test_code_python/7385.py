def solution():
    silver_weight = 3**3 * 6  # Calculate the weight of the silver cube
    silver_value = silver_weight * 25  # Calculate the value of the silver in the cube
    selling_price = silver_value * 1.10  # Calculate the selling price at 110% of its silver value
    result = selling_price
    return result

print(solution())