def solution():
    """Maurice is getting $2 for every finished task. And for every 10 tasks finished, he receives a $6 bonus. How much money would Maurice make for finishing 30 tasks?"""
    # Define the payment per task and the bonus payment
    PAYMENT_PER_TASK = 2
    BONUS_PAYMENT = 6

    # Initialize the counter for finished tasks and the bonus counter
    finished_tasks = 0
    bonus_counter = 0

    # Calculate the total payment for finishing 30 tasks
    for i in range(30):
        # Increment the finished tasks counter
        finished_tasks += 1
        
        # Check if the bonus condition is met, and add the bonus payment if it is
        if finished_tasks % 10 == 0:
            bonus_counter += 1

    total_payment = (finished_tasks * PAYMENT_PER_TASK) + (bonus_counter * BONUS_PAYMENT)

    result = total_payment
    return result

print(solution())