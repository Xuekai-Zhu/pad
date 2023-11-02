def solution():
    first_day_steps = 200 + 300
    second_day_steps = first_day_steps * 2
    third_day_steps = second_day_steps + 100

    # Add up the total number of steps for all three days
    total_steps = first_day_steps + second_day_steps + third_day_steps
    result = total_steps
    return result

print(solution())