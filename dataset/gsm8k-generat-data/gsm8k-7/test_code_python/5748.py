def solution():
    lakeview_pop = 24000
    seattle_pop = lakeview_pop - 4000
    boise_pop = (3/5) * seattle_pop
    total_pop = lakeview_pop + seattle_pop + boise_pop
    result = total_pop
    return result

print(solution())