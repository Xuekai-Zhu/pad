def solution():
    # Calculate the time it took for him to fix the kitchen counter
    time_kitchen = 3 * 8  # three times longer than the time he spent painting the house

    # Calculate the total time spent on the job
    total_time = 8 + 6 + time_kitchen  # time painting the house plus mowing the lawn plus fixing the counter

    # Calculate the total amount of money paid to Jerry
    total_money = total_time * 15  # $15 per hour of work

    result = total_money
    return result

print(solution())