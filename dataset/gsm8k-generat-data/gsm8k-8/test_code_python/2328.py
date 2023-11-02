def solution():
    # Calculate the sale price of the shoes
    sale_price = 51

    # Calculate the percentage of the original price that is the sale price
    percentage_off = 75

    # Calculate the original price of the shoes
    original_price = sale_price / (1 - percentage_off/100)
    result = original_price
    return result

print(solution())