def solution():
    """Maurice is getting $2 for every finished task. And for every 10 tasks finished, he receives a $6 bonus. How much money would Maurice make for finishing 30 tasks?"""
    # Define the payment for one task and the bonus for every 10 tasks
    TASK_PAYMENT = 2
    TASK_BONUS = 6

    # Define the number of tasks
    num_tasks = 30

    # Calculate the number of bonuses earned
    num_bonuses = num_tasks // 10

    # Calculate the total payment for tasks
    tasks_payment = num_tasks * TASK_PAYMENT

    # Calculate the total payment for bonuses
    bonuses_payment = num_bonuses * TASK_BONUS

    # Calculate the total payment
    total_payment = tasks_payment + bonuses_payment

    # Display the total payment
    result = total_payment
    return result

print(solution())