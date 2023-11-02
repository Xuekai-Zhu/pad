def solution():
    # Define the number of tires and the sale price
    num_tires = 4
    sale_price = 75

    # Calculate the total savings
    total_savings = 36

    # Calculate the original price of each tire
    original_price = (num_tires * sale_price - total_savings) / num_tires
    result = original_price
    return result

print(solution())