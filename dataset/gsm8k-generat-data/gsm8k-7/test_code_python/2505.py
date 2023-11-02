def solution():
    necklace_price = 34
    book_price = necklace_price + 5
    total_spent = necklace_price + book_price
    spending_limit = 70

    # Calculate how much Bob spent over the limit
    spent_over_limit = total_spent - spending_limit
    result = spent_over_limit
    return result

print(solution())