def solution():
    total_problems = 75
    completed_first_20_min = 10
    completed_second_20_min = 2 * completed_first_20_min

    remaining_time = 40  # minutes
    time_per_problem = remaining_time / (total_problems - completed_first_20_min - completed_second_20_min)

    remaining_problems = total_problems - completed_first_20_min - completed_second_20_min
    remaining_problems = max(0, remaining_problems)  # Make sure there are no negative remaining problems

    # Calculate how many problems can be completed in the remaining time
    completed_in_remaining_time = int(time_per_problem * remaining_time)

    # Calculate the final number of remaining problems
    remaining_problems -= completed_in_remaining_time
    result = remaining_problems
    return result

print(solution())