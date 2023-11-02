def solution():
    # Define the payment for one finished task and the bonus for 10 finished tasks
    payment_per_task = 2
    bonus_per_10_tasks = 6

    # Calculate the number of full 10-task sets completed
    full_sets = 30 // 10

    # Calculate the total payment for the finished tasks and bonuses
    total_payment = (30 * payment_per_task) + (full_sets * bonus_per_10_tasks)

    result = total_payment
    return result

print(solution())