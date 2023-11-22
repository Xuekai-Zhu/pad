def solution():
    
    # Define the number of pigs and the amount of feed they eat per day
    NUM_PIGS = 5
    FEED_PER_PIG = 4

    # Define the number of days in a week
    DAYS_IN_WEEK = 7

    # Calculate the total amount of feed eaten in a week
    total_feed_eaten = NUM_PIGS * FEED_PER_PIG * 2 * DAYS_IN_WEEK

    # Calculate the amount of feed left after a week
    feed_left = 300 - total_feed_eaten

    # Display the amount of feed left after a week
    result = feed_left
    return result

print(solution())