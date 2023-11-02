def solution():
    day_one = 2
    day_two = day_one * 2
    day_three = day_two * 2
    study_days = 6

    # Calculate the total number of sandwiches he will eat on the first three days
    total_sandwiches = day_one + day_two + day_three

    # Calculate the number of times he will eat that amount in 6 days
    sandwiches_per_cycle = total_sandwiches
    num_cycles = study_days // 3
    total_sandwiches += num_cycles * sandwiches_per_cycle

    # If there are any remaining days, calculate the extra sandwiches he will eat
    remaining_days = study_days % 3
    if remaining_days == 1:
        total_sandwiches += day_one
    elif remaining_days == 2:
        total_sandwiches += day_one + day_two

    result = total_sandwiches
    return result

print(solution())