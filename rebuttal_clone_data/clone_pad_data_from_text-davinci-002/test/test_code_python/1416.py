def solution():
    necklace_price = 34
    book_price = necklace_price + 5
    total_price = book_price + necklace_price
    limit = 70
    amount_over_limit = total_price - limit
    result = amount_over_limit
    return result

print(solution())