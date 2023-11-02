def solution():
    """Chelsea made 4 batches of cupcakes for the bake sale. The cupcakes took 20 minutes to bake and 30 minutes to ice per batch. How long did it take Chelsea to make the cupcakes?"""
    baking_time_per_batch = 20
    icing_time_per_batch = 30
    total_time = 4 * (baking_time_per_batch + icing_time_per_batch)
    result = total_time
    return result

print(solution())