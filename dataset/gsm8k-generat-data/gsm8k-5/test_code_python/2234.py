def solution():
    hours_per_day = 3  # Susie babysits for 3 hours per day
    rate_per_hour = 10  # Susie earns $10 per hour
    days_per_week = 7  # There are 7 days in a week

    # Calculate Susie's total earnings for last week
    total_earnings = hours_per_day * rate_per_hour * days_per_week

    # Calculate the amount Susie spent on a make-up set
    make_up_cost = total_earnings * (3/10)

    # Calculate the amount Susie spent on skincare products
    skincare_cost = total_earnings * (2/5)

    # Calculate the amount of money left from her earnings last week
    left_money = total_earnings - make_up_cost - skincare_cost
    result = left_money
    return result

print(solution())