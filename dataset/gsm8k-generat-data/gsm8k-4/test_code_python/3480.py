def solution():
    """Chelsea made 4 batches of cupcakes for the bake sale. The cupcakes took 20 minutes to bake and 30 minutes to ice per batch. How long did it take Chelsea to make the cupcakes?"""
    # Define the time to bake and ice a single batch of cupcakes
    BAKE_TIME = 20
    ICE_TIME = 30

    # Calculate the total time to make all batches of cupcakes
    total_time = (BAKE_TIME + ICE_TIME) * 4

    # return the result
    result = total_time
    return result

print(solution())