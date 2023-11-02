def solution():
    """There are four members in one household. Each member consumes 3 slices of bread during breakfast and 2 slices of bread for snacks. A loaf of bread has 12 slices. How many days will five loaves of bread last in this family?"""
    slices_per_day = (3 + 2) * 4
    slices_per_loaf = 12
    slices_per_five_loaves = slices_per_loaf * 5
    days = slices_per_five_loaves // slices_per_day
    result = days
    return result

print(solution())