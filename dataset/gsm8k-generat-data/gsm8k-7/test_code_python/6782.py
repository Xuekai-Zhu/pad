def solution():
    hendricks_price = 200
    discount = 0.2  # 20% discount from Gerald's price

    # Calculate the original price of the guitar (before the discount)
    original_price = hendricks_price / (1 - discount)

    result = original_price
    return result

print(solution())