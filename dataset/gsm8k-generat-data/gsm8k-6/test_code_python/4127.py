def solution():
    # Calculate the number of daisies sold on the second day
    daisies_second_day = 45 + 20  # 20 more flowers sold than on the first day

    # Calculate the number of daisies sold on the third day
    daisies_third_day = 2 * daisies_second_day - 10  # 10 less than twice the flowers sold than on the second day

    # Calculate the number of daisies sold on the fourth day
    daisies_fourth_day = 350 - 45 - daisies_second_day - daisies_third_day  # total daisies sold minus daisies sold on first 3 days

    result = daisies_fourth_day
    return result

print(solution())