def solution():
    apples_per_wheel = 3
    wheels_per_month = 1
    months_per_year = 12

    # Calculate the total number of wheels that need to be replaced in a year
    total_wheels = wheels_per_month * months_per_year

    # Calculate the number of golden apples needed to pay for the first 6 months
    apples_for_half_year = apples_per_wheel * (total_wheels / 2)

    # Calculate the number of golden apples needed to pay for the remaining 6 months (at twice the rate)
    apples_for_second_half = apples_per_wheel * (total_wheels / 2) * 2

    # Calculate the total number of golden apples needed for the entire year
    total_apples = apples_for_half_year + apples_for_second_half
    result = total_apples
    return result

print(solution())