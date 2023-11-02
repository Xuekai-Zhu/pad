def solution():
    """Norma takes her clothes to the laundry. She leaves 9 T-shirts and twice as many sweaters as T-shirts in the washer. When she returns she finds 3 sweaters and triple the number of T-shirts. How many items are missing?"""
    t_shirts = 9
    sweaters = t_shirts * 2
    missing_t_shirts = (t_shirts * 3) - 3
    missing_sweaters = sweaters - 3
    total_missing_items = missing_t_shirts + missing_sweaters
    result = total_missing_items
    return result

print(solution())