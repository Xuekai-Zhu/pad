def solution():
    """Gina's snake eats one mouse every 4 weeks. How many mice will it eat in a decade?"""
    mice_per_week = 1/4
    weeks_per_year = 52
    mice_per_year = mice_per_week * weeks_per_year
    mice_per_decade = mice_per_year * 10
    result = mice_per_decade
    return result

print(solution())