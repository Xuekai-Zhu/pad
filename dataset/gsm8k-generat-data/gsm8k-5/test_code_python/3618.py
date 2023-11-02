def solution():
    tasks = 30  # Maurice has to finish 30 tasks
    payment_per_task = 2  # Maurice gets $2 for every finished task
    bonus_per_10_tasks = 6  # Maurice gets $6 as a bonus for every 10 tasks finished

    # Calculate the total payment for finished tasks
    payment_for_tasks = tasks * payment_per_task

    # Calculate the number of bonuses Maurice gets
    bonuses = tasks // 10

    # Calculate the total bonus payment
    bonus_payment = bonuses * bonus_per_10_tasks

    # Calculate the total payment for all tasks
    total_payment = payment_for_tasks + bonus_payment
    result = total_payment
    return result

print(solution())