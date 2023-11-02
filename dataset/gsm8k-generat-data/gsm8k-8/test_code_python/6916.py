def solution():
    # Calculate the original selling price of the book
    original_price = 50 / (1 + 0.3)

    # Calculate the selling price after the discount
    discount_price = original_price * 0.9

    # Calculate the profit percentage
    profit_percentage = (discount_price - original_price) / original_price * 100
    result = profit_percentage
    return result

print(solution())