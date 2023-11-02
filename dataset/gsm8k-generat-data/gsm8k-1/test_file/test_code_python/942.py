def solution():
    """A bakery has 40 less than seven times as many loaves of bread as Sam had last Friday. If Sam had seventy loaves of bread last Friday, how many loaves of bread does the bakery have?"""
    sam_loaves = 70
    bakery_loaves = 7 * sam_loaves - 40
    result = bakery_loaves
    return result

print(solution())