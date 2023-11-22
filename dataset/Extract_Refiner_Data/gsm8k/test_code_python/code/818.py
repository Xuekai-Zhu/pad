def solution():
    
    # Define the number of cycles and tasks per cycle
    cycles_per_day = 30
    tasks_per_cycle = 5

    # Define the pay per task
    pay_per_task = 1.20

    # Calculate the total pay per day
    pay_per_day = cycles_per_day * tasks_per_cycle * pay_per_task

    # Calculate the total pay for 7 days
    pay_per_week = pay_per_day * 7

    # return the result
    result = pay_per_week
    return result

print(solution())