def solution():
    initial_caterpillars = 14
    hatched_caterpillars = 4
    leaving_caterpillars = 8

    # Calculate the total number of caterpillars after the changes
    total_caterpillars = initial_caterpillars + hatched_caterpillars - leaving_caterpillars
    result = total_caterpillars
    return result

print(solution())