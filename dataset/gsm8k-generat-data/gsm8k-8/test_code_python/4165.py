def solution():
    # Define the number of sandwiches eaten on each of the first three days
    day1_sandwiches = 2
    day2_sandwiches = day1_sandwiches * 2
    day3_sandwiches = day2_sandwiches * 2

    # Calculate the total number of sandwiches eaten in the first three days
    total_sandwiches_first_three_days = day1_sandwiches + day2_sandwiches + day3_sandwiches

    # Define the number of days Paul studies
    study_days = 6

    # Calculate the number of times Paul eats sandwiches in the study period
    sandwich_periods = study_days // 3

    # Calculate the total number of sandwiches eaten during the study period
    total_sandwiches_study_period = total_sandwiches_first_three_days * sandwich_periods

    # Add any additional sandwiches eaten on the last partial period
    remainder_days = study_days % 3
    if remainder_days == 1:
        total_sandwiches_study_period += day1_sandwiches
    elif remainder_days == 2:
        total_sandwiches_study_period += day1_sandwiches + day2_sandwiches

    result = total_sandwiches_study_period
    return result

print(solution())