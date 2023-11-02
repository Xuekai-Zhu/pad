def solution():
    hours_per_day = 3
    rate_per_hour = 10
    num_days = 7

    # Calculate total earnings for the week
    total_earnings = hours_per_day * rate_per_hour * num_days

    # Calculate the amount spent on make-up
    makeup_cost = 3/10 * total_earnings

    # Calculate the amount spent on skincare products
    skincare_cost = 2/5 * total_earnings

    # Calculate the amount left from earnings
    left_earnings = total_earnings - makeup_cost - skincare_cost
    result = left_earnings
    return result

print(solution())