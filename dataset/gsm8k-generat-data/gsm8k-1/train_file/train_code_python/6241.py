def solution():
    """Tim drinks 2 bottles that are each 1.5 quarts and an additional 20 ounces a day. How much water does he drink a week?"""
    bottles_per_day = 2
    bottle_size = 1.5 * 32 # convert quarts to ounces
    additional_ounces_per_day = 20
    ounces_per_week = (bottles_per_day * bottle_size + additional_ounces_per_day) * 7
    result = ounces_per_week
    return result

print(solution())