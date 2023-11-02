def solution():
    """How many shirts should Shenny pack for her next vacation if she's planning to use the same shirt when departing on Monday and returning on Sunday and two different shirts each other day?"""
    total_days = 7
    shirts_needed = 1 + 2 * (total_days - 2)
    result = shirts_needed
    return result

print(solution())