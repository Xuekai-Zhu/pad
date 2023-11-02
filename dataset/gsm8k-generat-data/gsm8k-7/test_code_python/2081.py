def solution():
    days_base = 14
    grades_below_b = 4
    extra_days_per_grade = 3

    # Calculate the total number of extra days Cassidy will be grounded for
    extra_days = grades_below_b * extra_days_per_grade

    # Calculate the total number of days Cassidy will be grounded for
    total_days = days_base + extra_days
    result = total_days
    return result

print(solution())