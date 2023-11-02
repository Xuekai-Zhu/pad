def solution():
    """If Lucy would give Linda $5, Lucy would have the same amount of money as Linda. If Lucy originally had $20, how much money did Linda have at the beginning?"""
    lucy_start = 20
    lucy_end = lucy_start - 5
    linda_end = lucy_end
    linda_start = linda_end + 5
    result = linda_start
    return result

print(solution())