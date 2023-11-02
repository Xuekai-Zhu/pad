def solution():
    
    lake_view_pop = 24000
    seattle_pop = lake_view_pop - 4000
    boise_pop = (3/5) * seattle_pop
    total_pop = lake_view_pop + seattle_pop + boise_pop
    result = total_pop
    return result

print(solution())