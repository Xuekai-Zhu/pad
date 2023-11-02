def solution():
    hours_per_day = 8  # Ben works 8-hour shifts
    hours_per_chair = 5  # It takes Ben 5 hours to build 1 rocking chair
    days = 10  # Ben wants to know how many chairs he can build in 10 days

    # Calculate the total number of hours Ben will work in 10 days
    total_hours = hours_per_day * days

    # Calculate the total number of chairs Ben can build in 10 days
    total_chairs = total_hours // hours_per_chair
    result = total_chairs
    return result

print(solution())