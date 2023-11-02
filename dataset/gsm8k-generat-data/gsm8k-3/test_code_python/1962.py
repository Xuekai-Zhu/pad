def solution():
    """Philip is a painter. He makes 2 paintings per day. If he already has 20 paintings, how many paintings in total will he have after 30 days?"""
    # Define the number of paintings Philip makes per day and the number of days
    PAINTINGS_PER_DAY = 2
    NUM_DAYS = 30

    # Define the number of paintings Philip already has
    current_paintings = 20

    # Calculate the total number of paintings Philip will have after 30 days
    total_paintings = current_paintings + (PAINTINGS_PER_DAY * NUM_DAYS)

    # Display the total number of paintings
    result = total_paintings
    return result

print(solution())