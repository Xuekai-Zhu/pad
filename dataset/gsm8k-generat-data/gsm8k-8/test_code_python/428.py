def solution():
    # Calculate the number of eggs laid on the second day
    eggs_on_second_day = 50 * 2

    # Calculate the number of eggs laid on the third day
    eggs_on_third_day = eggs_on_second_day + 20

    # Calculate the total number of eggs laid on the first three days
    eggs_on_first_three_days = 50 + eggs_on_second_day + eggs_on_third_day

    # Calculate the total number of eggs laid on the fourth day
    eggs_on_fourth_day = eggs_on_first_three_days * 2

    # Calculate the total number of eggs laid over the span of the four days
    total_eggs_laid = 50 + eggs_on_second_day + eggs_on_third_day + eggs_on_fourth_day

    result = total_eggs_laid
    return result

print(solution())