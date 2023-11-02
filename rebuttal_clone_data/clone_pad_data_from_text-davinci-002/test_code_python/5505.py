def solution():
    total_caterpillars = 14
    hatched_caterpillars = 4
    cocooned_caterpillars = 8
    remaining_caterpillars = total_caterpillars + hatched_caterpillars - cocooned_caterpillars
    result = remaining_caterpillars
    return result

print(solution())