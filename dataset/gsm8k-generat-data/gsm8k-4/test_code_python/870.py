def solution():
    """Matthew, the baker, arrives at work early every morning to make his famous caramel-apple coffee cakes for the day.  It usually takes Matthew 1 hour to assemble ingredients, 1.5 hours to bake the cakes, and another 1 hour to decorate each cake with cinnamon sprinkles.  One day, Matthew's oven failed to reach the correct temperature and it took twice as long for the cakes to bake as they usually take.  On that day, how long did it take, in hours, for Matthew to make his famous caramel-apple coffee cakes?"""
    # Calculate the total time to make a cake without oven failure
    total_time_without_failure = 1 + 1.5 + 1

    # Calculate the total time for the day with oven failure
    total_time_with_failure = 1 + 3 + 1

    # Calculate the total time to make all the cakes for the day with oven failure
    total_time_for_day = total_time_with_failure * 12

    result = total_time_for_day
    return result

print(solution())