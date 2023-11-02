def solution():
    """Lynne bought 7 books about cats and 2 books about the solar system. She also bought 3 magazines. Each book costs $7 and each magazine costs $4. How much did Lynne spend in all?"""
    num_cat_books = 7
    num_solar_books = 2
    num_magazines = 3
    cost_per_book = 7
    cost_per_magazine = 4
    total_spent_books = (num_cat_books + num_solar_books) * cost_per_book
    total_spent_magazines = num_magazines * cost_per_magazine
    total_spent = total_spent_books + total_spent_magazines
    result = total_spent
    return result

print(solution())