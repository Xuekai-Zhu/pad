def solution():
    price = 184

    discount = 0.08  # 8% discount

    # Calculate the original price of the shoes
    original_price = price / (1 - discount)

    # Calculate the amount saved by Shara
    amount_saved = original_price - price
    result = amount_saved
    return result

print(solution())