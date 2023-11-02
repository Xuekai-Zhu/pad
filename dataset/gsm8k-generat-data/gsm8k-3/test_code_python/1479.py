def solution():
    """Wallace runs a beef jerky company. The company dries the jerky low and slow, so one batch of jerky takes all night to make. Each batch can make 10 bags of jerky. Wallace received a customer order for 60 bags of jerky. If he has 20 bags of jerky already made, how many days will it be before he can fulfill the customer’s order?"""
    # Define the number of bags of jerky Wallace can make per batch
    BAGS_PER_BATCH = 10

    # Define the number of bags of jerky already made
    bags_already_made = 20

    # Define the number of bags still needed to fulfill the order
    bags_needed = 60 - bags_already_made

    # Calculate the number of batches needed to fulfill the order
    batches_needed = bags_needed / BAGS_PER_BATCH

    # Round up to the nearest integer
    batches_needed = math.ceil(batches_needed)

    # Calculate the number of days it will take to make the jerky
    days_needed = batches_needed * 1 # one night per batch

    # Display the number of days needed
    result = days_needed
    return result

print(solution())