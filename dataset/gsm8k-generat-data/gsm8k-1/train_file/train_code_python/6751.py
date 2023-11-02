def solution():
    """Cassandra bought four dozen Granny Smith apples and used them to make four apple pies. She cut each pie into 6 large pieces. How many apples are in each slice of pie?"""
    apples_per_dozen = 12
    total_apples = 4 * apples_per_dozen
    pies = 4
    slices_per_pie = 6
    apples_per_slice = total_apples / (pies * slices_per_pie)
    result = apples_per_slice
    return result

print(solution())