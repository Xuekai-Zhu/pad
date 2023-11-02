def solution():
    ashland_population = 21263
    min_division_size = 10000
    max_division_size = 25000
    if ashland_population < min_division_size or ashland_population > max_division_size:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())