def solution():
    current_age_diane = 16  # Diane is 16 years old now
    age_difference_da = 14  # Diane will be 30 in 14 years
    age_difference_dx = age_difference_da / 2  # Alex is currently twice older than Diane will be when she is 30
    age_difference_ax = age_difference_dx + age_difference_da  # Alex is older than Diane by the same amount he will be older than her when she is 30
    current_age_allison = current_age_diane / 2  # Allison is currently half as old as Diane

    # Calculate the sum of the ages of Alex and Allison now
    sum_ages = current_age_allison + age_difference_ax
    result = sum_ages
    return result

print(solution())