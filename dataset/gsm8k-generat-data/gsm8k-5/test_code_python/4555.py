def solution():
    eggs_per_day = 2  # Maddy eats 2 chocolate eggs per day after school
    days_per_week = 5  # Maddy has school for 5 days in a week

    # Calculate the number of weeks the chocolate eggs will last
    weeks = 40 / (eggs_per_day * days_per_week)

    result = weeks
    return result

print(solution())