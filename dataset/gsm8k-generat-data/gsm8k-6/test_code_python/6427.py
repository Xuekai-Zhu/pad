def solution():
    # Calculate the total number of days John spends on jury duty
    trial_length = 4 * 2  # trial lasts 4 times as long as jury selection, which takes 2 days
    deliberation_length = 6 * 16  # they spend 16 hours a day in deliberation for 6 full days
    total_length = trial_length + deliberation_length / 24  # add the trial length and deliberation length (converted from hours to days)
    result = total_length
    return result.round(2)  # round to 2 decimal places to account for partial days

print(solution())