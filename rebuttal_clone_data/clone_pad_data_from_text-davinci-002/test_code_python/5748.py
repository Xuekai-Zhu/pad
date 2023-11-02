def solution():
    seattle_population = 24000
    boise_population = seattle_population * (3/5)
    lake_view_population = seattle_population + 4000
    total_population = seattle_population + boise_population + lake_view_population
    result = total_population
    return result

print(solution())