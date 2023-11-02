def solution():
    # Calculate the profits for the first, third, and fourth quarter
    profits_first_quarter = 1500
    profits_third_quarter = 3000
    profits_fourth_quarter = 2000

    # Calculate the total profits for the year
    total_profits = 8000

    # Calculate the profits for the second quarter
    profits_second_quarter = total_profits - profits_first_quarter - profits_third_quarter - profits_fourth_quarter
    result = profits_second_quarter
    return result

print(solution())