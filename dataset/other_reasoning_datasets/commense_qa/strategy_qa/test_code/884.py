def solution():
    milky_way_stars = 200 billion
    earth_population = 7.5 billion
    if milky_way_stars >= (10 * earth_population):
        result = "yes"
    else:
        result = "no"
    return result

print(solution())