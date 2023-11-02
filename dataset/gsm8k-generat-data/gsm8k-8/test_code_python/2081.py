def solution():
    # Define the number of days for each grade below a B
    days_per_grade = 3

    # Define the number of grades below a B
    grades_below_B = 4

    # Calculate the total number of extra days
    extra_days = grades_below_B * days_per_grade

    # Calculate the total number of days grounded
    total_days = 14 + extra_days

    result = total_days
    return result

print(solution())