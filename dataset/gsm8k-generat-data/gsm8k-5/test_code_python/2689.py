def solution():
    years_calculus = 4  # Devin taught Calculus for 4 years
    years_algebra = 2 * years_calculus  # Devin taught Algebra for twice as many years as Calculus
    years_statistics = 5 * years_algebra  # Devin taught Statistics for 5 times as many years as Algebra

    # Calculate the total number of years Devin has taught
    total_years = years_calculus + years_algebra + years_statistics
    result = total_years
    return result

print(solution())