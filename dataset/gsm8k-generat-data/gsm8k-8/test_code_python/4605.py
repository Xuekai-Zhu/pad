def solution():
    # Calculate the total number of eggs produced in a week
    total_eggs = 10 * 6

    # Calculate the total number of dozens of eggs produced in a week
    dozens_of_eggs = total_eggs / 12

    # Calculate the total amount of money made in a week
    money_in_one_week = dozens_of_eggs * 2

    # Calculate the total amount of money made in 2 weeks
    money_in_two_weeks = money_in_one_week * 2

    result = money_in_two_weeks
    return result

print(solution())