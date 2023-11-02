def solution():
    """The price of a book was $400. If the book's price is decreased by 15% and then increased by 40%, what is the final price of the book?"""
    original_price = 400
    first_discount = 0.15
    first_price = original_price * (1 - first_discount)
    second_increase = 0.4
    final_price = first_price * (1 + second_increase)
    result = final_price
    return result

print(solution())