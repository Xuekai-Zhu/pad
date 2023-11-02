def solution():
    num_cities = 21
    num_days = 30
    num_arrests_per_day = 10
    pre_trial_days = 4
    half_sentence_weeks = 1

    # Calculate the total number of arrests
    total_arrests = num_cities * num_days * num_arrests_per_day

    # Calculate the total number of days spent in jail before trial
    total_pre_trial_days = total_arrests * pre_trial_days

    # Calculate the total number of weeks spent in jail for the sentence
    total_sentence_weeks = total_arrests * (half_sentence_weeks / 2)

    # Convert the total sentence weeks to days
    total_sentence_days = total_sentence_weeks * 7

    # Calculate the total combined weeks of jail time
    total_weeks = (total_pre_trial_days + total_sentence_days) / 7

    result = total_weeks
    return result

print(solution())