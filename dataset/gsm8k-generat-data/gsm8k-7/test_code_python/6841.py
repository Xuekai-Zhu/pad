def solution():
    num_multivitamins_per_day = 2
    num_calcium_supplements_first_2_weeks = 3
    num_calcium_supplements_last_2_weeks = 1
    num_days_in_month = 30

    # Calculate the total number of multivitamins that Janet will take in the month
    total_multivitamins = num_multivitamins_per_day * num_days_in_month

    # Calculate the total number of calcium supplements that Janet will take in the first 2 weeks
    total_calcium_supplements_first_2_weeks = num_calcium_supplements_first_2_weeks * 14

    # Calculate the total number of calcium supplements that Janet will take in the last 2 weeks
    total_calcium_supplements_last_2_weeks = num_calcium_supplements_last_2_weeks * 14

    # Calculate the total number of all pills that Janet will take in the month
    total_pills = total_multivitamins + total_calcium_supplements_first_2_weeks + total_calcium_supplements_last_2_weeks
    result = total_pills
    return result

print(solution())