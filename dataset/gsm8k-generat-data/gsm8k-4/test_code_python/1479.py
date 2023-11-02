def solution():
    """Wallace runs a beef jerky company. The company dries the jerky low and slow, so one batch of jerky takes all night to make. Each batch can make 10 bags of jerky. Wallace received a customer order for 60 bags of jerky. If he has 20 bags of jerky already made, how many days will it be before he can fulfill the customer’s order?"""
    # Define the number of bags per batch
    BAGS_PER_BATCH = 10

    # Define the number of bags already made
    bags_already_made = 20

    # Define the number of bags needed to fulfill the order
    bags_needed = 60

    # Calculate the number of batches needed to fulfill the order
    batches_needed = (bags_needed - bags_already_made) / BAGS_PER_BATCH

    # Calculate the number of days needed to make the batches
    days_needed = batches_needed * 1

    result = int(days_needed)
    return result

print(solution())