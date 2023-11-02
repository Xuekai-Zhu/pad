def solution():
    starting_amount = 20
    weekly_increase = 10
    num_weeks_in_month = 4

    # Calculate the total amount saved after a month
    total_amount_saved = starting_amount + (weekly_increase * (num_weeks_in_month - 1))

    result = total_amount_saved
    return result

print(solution())