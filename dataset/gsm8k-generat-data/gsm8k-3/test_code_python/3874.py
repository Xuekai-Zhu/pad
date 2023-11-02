def solution():
    """Sara makes cakes during the five weekdays to sell on weekends. She makes 4 cakes a day and sells her cakes for $8. In 4 weeks she managed to sell all the cakes. How much money did she collect during that time?"""
    # Define the number of weekdays and cakes made per day
    WEEKDAYS = 5
    CAKES_PER_DAY = 4

    # Calculate the total number of cakes made in 4 weeks
    total_cakes = CAKES_PER_DAY * WEEKDAYS * 4

    # Calculate the total amount collected for selling all the cakes
    total_amount_collected = total_cakes * 8

    # Display the total amount collected
    result = total_amount_collected
    return result

print(solution())