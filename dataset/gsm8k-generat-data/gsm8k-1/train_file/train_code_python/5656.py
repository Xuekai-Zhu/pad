def solution():
    """Gina's snake eats one mouse every 4 weeks. How many mice will it eat in a decade?"""
    mice_per_week = 1/4
    weeks_per_year = 52
    years_per_decade = 10
    total_mice = mice_per_week * weeks_per_year * years_per_decade
    result = total_mice
    return result

print(solution())