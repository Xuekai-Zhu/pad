def solution():
    """Jake trips over his dog 40% percent of mornings. 25% of the time he trips, he drops his coffee. What percentage of mornings does he NOT drop his coffee?"""
    # Define the probability of Jake tripping over his dog and dropping his coffee
    P_TRIP_AND_DROP = 0.4 * 0.25

    # Calculate the probability of Jake not dropping his coffee
    P_NOT_DROP = 1 - P_TRIP_AND_DROP

    # Convert the probability to a percentage
    percentage = P_NOT_DROP * 100

    # Display the percentage
    result = percentage
    return result

print(solution())