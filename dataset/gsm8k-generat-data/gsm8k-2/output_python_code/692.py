def solution():
    """Ian had twenty roses. He gave six roses to his mother, nine roses to his grandmother, four roses to his sister, and he kept the rest. How many roses did Ian keep?"""
    total_roses = 20
    roses_given = 6 + 9 + 4
    roses_kept = total_roses - roses_given
    result = roses_kept
    return result

print(solution())