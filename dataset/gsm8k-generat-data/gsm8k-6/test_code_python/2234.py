def solution():
    # Calculate Susie's earnings for last week
    earnings = 10 * 3 * 7  # $10 per hour, 3 hours a day, 7 days in a week

    # Calculate the amount of money she spent on the make-up set
    makeup_cost = earnings * (3/10)

    # Calculate the amount of money she spent on skincare products
    skincare_cost = earnings * (2/5)

    # Calculate the amount of money she has left from her earnings last week
    remaining_earnings = earnings - makeup_cost - skincare_cost
    result = remaining_earnings
    return result

print(solution())