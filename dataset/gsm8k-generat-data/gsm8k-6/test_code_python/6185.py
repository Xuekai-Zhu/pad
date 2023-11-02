def solution():
    # Calculate the total number of coolers produced per hour
    coolers_per_hour = 90 + 70

    # Calculate the total number of products produced per hour
    products_per_hour = 90 + coolers_per_hour

    # Calculate the total number of products produced in 1 day
    products_per_day = products_per_hour * 9

    # Calculate the total number of products produced in 5 days
    products_per_5_days = products_per_day * 5

    result = products_per_5_days
    return result

print(solution())