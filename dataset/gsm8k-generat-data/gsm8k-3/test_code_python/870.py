def solution():
    """Matthew, the baker, arrives at work early every morning to make his famous caramel-apple coffee cakes for the day.  It usually takes Matthew 1 hour to assemble ingredients, 1.5 hours to bake the cakes, and another 1 hour to decorate each cake with cinnamon sprinkles.  One day, Matthew's oven failed to reach the correct temperature and it took twice as long for the cakes to bake as they usually take.  On that day, how long did it take, in hours, for Matthew to make his famous caramel-apple coffee cakes?"""
    # Define the time it takes Matthew for each step
    INGREDIENTS_TIME = 1
    BAKE_TIME = 1.5
    DECORATE_TIME = 1

    # Calculate the total time it takes Matthew to make a cake
    total_time = INGREDIENTS_TIME + BAKE_TIME + DECORATE_TIME

    # Calculate the new bake time when the oven fails
    new_bake_time = BAKE_TIME * 2

    # Calculate the new total time when the oven fails
    new_total_time = INGREDIENTS_TIME + new_bake_time + DECORATE_TIME

    # Calculate the total time it takes Matthew to make a cake when the oven fails
    total_time_when_fail = new_total_time - total_time

    # Display the total time it takes Matthew to make his famous caramel-apple coffee cakes when the oven fails
    result = total_time + total_time_when_fail
    return result

print(solution())