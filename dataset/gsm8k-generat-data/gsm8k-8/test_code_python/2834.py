def solution():
    # Define the number of math problems Marvin practiced yesterday
    marvin_yesterday = 40

    # Calculate the number of math problems Marvin practiced today
    marvin_today = 3 * marvin_yesterday

    # Define the number of math problems Arvin practiced today and yesterday
    arvin_both_days = 2 * (marvin_today + marvin_yesterday)

    # Calculate the total number of math problems practiced
    total_problems = marvin_today + marvin_yesterday + arvin_both_days
    result = total_problems
    return result

print(solution())