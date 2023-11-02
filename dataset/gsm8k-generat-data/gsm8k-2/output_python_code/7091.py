def solution():
    """Jon’s textbooks weigh three times as much as Brandon’s textbooks. Jon has four textbooks that weigh two, eight, five and nine pounds respectively. How much do Brandon’s textbooks weigh?"""
    jons_books_weight = sum([2, 8, 5, 9])
    brandons_books_weight = jons_books_weight / 3
    result = brandons_books_weight
    return result

print(solution())