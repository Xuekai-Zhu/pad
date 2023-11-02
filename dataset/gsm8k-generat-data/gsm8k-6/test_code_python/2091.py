def solution():
    # Calculate the original price of the shoes
    original_price = 184 / (1 - 8/100)  # using the formula: original price = discounted price / (1 - discount percentage)

    # Calculate the amount Shara saved
    amount_saved = original_price - 184
    result = amount_saved
    return result

print(solution())