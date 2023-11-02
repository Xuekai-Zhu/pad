def solution():
    # Find the number of years Devin taught Calculus
    years_calculus = 4

    # Find the number of years Devin taught Algebra
    years_algebra = years_calculus * 2

    # Find the number of years Devin taught Statistics
    years_statistics = years_algebra * 5

    # Find the total number of years Devin has taught
    total_years = years_calculus + years_algebra + years_statistics
    result = total_years
    return result

print(solution())