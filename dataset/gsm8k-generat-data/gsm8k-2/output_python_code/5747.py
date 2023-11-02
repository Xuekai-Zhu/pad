def solution():
    """There are 3/5 times as many people living in Boise as the number living in Seattle. There are 4000 more people in Lake View than the population in Seattle. If Lake View's population is 24000, calculate the total population of the three cities."""
    lake_view_pop = 24000
    seattle_pop = lake_view_pop - 4000
    boise_pop = (3/5) * seattle_pop
    total_pop = lake_view_pop + seattle_pop + boise_pop
    result = total_pop
    return result

print(solution())