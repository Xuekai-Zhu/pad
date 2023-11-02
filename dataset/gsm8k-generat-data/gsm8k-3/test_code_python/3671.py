def solution():
    """Diana needs to bike 10 miles to get home.  She can bike 3 mph for two hours before she gets tired, and she can bike 1 mph until she gets home.  How long will it take Diana to get home?"""
    # Define the distance Diana needs to bike
    distance = 10

    # Calculate the time Diana can bike at 3 mph
    time1 = 2

    # Calculate the remaining distance Diana needs to bike
    remaining_distance = distance - (3 * time1)

    # Calculate the time Diana can bike at 1 mph to cover the remaining distance
    time2 = remaining_distance / 1

    # Calculate the total time Diana needs to bike
    total_time = time1 + time2

    # Display the total time
    result = total_time
    return result

print(solution())