def solution():
    original_price = 350  # The original price of the dress
    sale_price = 140  # The sale price of the dress

    # Calculate the percentage off
    percentage_off = ((original_price - sale_price) / original_price) * 100
    result = percentage_off
    return result

print(solution())