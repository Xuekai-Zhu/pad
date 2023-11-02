def solution():
    """A loaf of bread has 24 slices. If Abby can eat 2 slices a day while Josh can eat twice as much, how many days will the loaf of bread last?"""
    total_slices = 24
    abby_slices_per_day = 2
    josh_slices_per_day = 4
    slices_per_day = abby_slices_per_day + josh_slices_per_day
    days_last = total_slices / slices_per_day
    result = days_last
    return result

print(solution())