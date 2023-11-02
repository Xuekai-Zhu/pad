def solution():
    """Milly needs to return a book she decided was really boring. The book weighs 4 pounds, cost $32, and needs to be returned to a distribution center 20 miles away. If the shipping company charges $0.35 per pound plus $0.08 per mile, and Amazon will only refund 75% of the book's purchase price, how much money will Milly lose?"""
    book_weight = 4
    shipping_rate_per_pound = 0.35
    shipping_rate_per_mile = 0.08
    shipping_cost = book_weight * shipping_rate_per_pound + 20 * shipping_rate_per_mile
    book_refund = 32 * 0.75
    total_cost = shipping_cost + (32 - book_refund)
    result = total_cost
    return result

print(solution())