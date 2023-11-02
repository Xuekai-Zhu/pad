def solution():
    """Norma takes her clothes to the laundry. She leaves 9 T-shirts and twice as many sweaters as T-shirts in the washer. When she returns she finds 3 sweaters and triple the number of T-shirts. How many items are missing?"""
    t_shirts = 9
    sweaters = 2 * t_shirts
    t_shirts_back = 3 * sweaters
    sweaters_back = t_shirts
    missing_items = (t_shirts + sweaters) - (t_shirts_back + sweaters_back)
    result = missing_items
    return result

print(solution())