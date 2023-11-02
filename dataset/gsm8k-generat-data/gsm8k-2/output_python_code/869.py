def solution():
    """Matthew, the baker, arrives at work early every morning to make his famous caramel-apple coffee cakes for the day.
    It usually takes Matthew 1 hour to assemble ingredients, 1.5 hours to bake the cakes, and another 1 hour to decorate each cake with cinnamon sprinkles.
    One day, Matthew's oven failed to reach the correct temperature and it took twice as long for the cakes to bake as they usually take.
    On that day, how long did it take, in hours, for Matthew to make his famous caramel-apple coffee cakes?"""
    ingredients_time = 1
    normal_bake_time = 1.5
    sprinkle_time = 1
    failed_bake_time = 2 * normal_bake_time
    total_time = ingredients_time + failed_bake_time + sprinkle_time
    result = total_time
    return result

print(solution())