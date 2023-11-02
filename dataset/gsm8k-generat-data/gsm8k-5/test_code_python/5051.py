def solution():
    # Calculate the total number of steps for the first day
    day_one_steps = 200 + 300

    # Calculate the total number of steps for the second day
    day_two_steps = day_one_steps * 2

    # Calculate the total number of steps for the third day
    day_three_steps = day_two_steps + 100

    # Calculate the total number of steps for all three days
    total_steps = day_one_steps + day_two_steps + day_three_steps
    result = total_steps
    return result

print(solution())