def solution():
    tshirts = 9  # Norma leaves 9 T-shirts
    sweaters = 2 * tshirts  # Norma leaves twice as many sweaters as T-shirts

    # When Norma returns, she finds 3 sweaters and triple the number of T-shirts
    new_sweaters = 3
    new_tshirts = 3 * tshirts

    # Calculate the number of missing items
    missing_items = (tshirts + sweaters) - (new_tshirts + new_sweaters)
    result = missing_items
    return result

print(solution())