def solution():
    """Ali's class wants to order 35 English textbooks and 35 geography textbooks. Knowing that a geography book costs $10.50 and that an English book costs $7.50, what is the amount of this order?"""
    num_english_books = 35
    num_geography_books = 35
    cost_english_book = 7.5
    cost_geography_book = 10.5
    total_cost = (num_english_books * cost_english_book) + (num_geography_books * cost_geography_book)
    result = total_cost
    return result

print(solution())