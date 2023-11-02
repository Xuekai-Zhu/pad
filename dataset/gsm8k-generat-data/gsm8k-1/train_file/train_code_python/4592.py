def solution():
    """Brittany uses 1/4 ounce of shampoo to wash her hair every other day. She buys shampoo in 14-ounce bottles. How many bottles does she need to get her through a leap year?"""
    shampoo_per_use = 1/4
    uses_per_day = 1/2
    ounces_per_year = shampoo_per_use * uses_per_day * 366
    bottles_needed = ounces_per_year / 14
    result = bottles_needed
    return result

print(solution())