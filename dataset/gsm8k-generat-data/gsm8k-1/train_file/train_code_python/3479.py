def solution():
    """Chelsea made 4 batches of cupcakes for the bake sale. The cupcakes took 20 minutes to bake and 30 minutes to ice per batch. How long did it take Chelsea to make the cupcakes?"""
    batches = 4
    baking_time = 20
    icing_time = 30
    total_time = (baking_time + icing_time) * batches
    result = total_time
    return result

print(solution())