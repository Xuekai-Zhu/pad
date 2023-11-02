def solution():
    # Calculate the total number of arrests
    total_arrests = 30 * 10 * 21

    # Calculate the total number of days in jail before trial
    pre_trial_days = total_arrests * 4

    # Calculate the total number of weeks for half of the sentence
    sentence_weeks = (7 * 2) / 2

    # Calculate the total number of weeks in jail
    total_weeks = (pre_trial_days + (30 * total_arrests * sentence_weeks)) / 7
    result = total_weeks
    return result

print(solution())