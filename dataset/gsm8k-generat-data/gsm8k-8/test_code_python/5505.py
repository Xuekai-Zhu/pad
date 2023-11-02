def solution():
    initial_caterpillars = 14
    newly_hatched_caterpillars = 4
    leaving_caterpillars = 8

    caterpillars_left = initial_caterpillars + newly_hatched_caterpillars - leaving_caterpillars
    result = caterpillars_left
    return result

print(solution())