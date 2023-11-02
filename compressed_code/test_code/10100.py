def solution():
    
    starting_caterpillars = 14
    hatched_caterpillars = 4
    leaving_caterpillars = 8
    remaining_caterpillars = starting_caterpillars + hatched_caterpillars - leaving_caterpillars
    result = remaining_caterpillars
    return result

print(solution())