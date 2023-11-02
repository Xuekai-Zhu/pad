def solution():
    """There are four members in one household. Each member consumes 3 slices of bread during breakfast and 2 slices of bread for snacks. 
    A loaf of bread has 12 slices. How many days will five loaves of bread last in this family?"""
    members = 4
    breakfast_slices = 3
    snack_slices = 2
    slices_per_day = members * (breakfast_slices + snack_slices)
    slices_per_loaf = 12
    loaves_per_day = slices_per_day / slices_per_loaf
    loaves_per_week = loaves_per_day * 7
    loaves_needed = 5
    days_lasting = loaves_needed / loaves_per_week
    
    result = days_lasting
    return result

print(solution())