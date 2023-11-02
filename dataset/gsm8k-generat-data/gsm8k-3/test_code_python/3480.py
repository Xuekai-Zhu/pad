def solution():
    """Chelsea made 4 batches of cupcakes for the bake sale. The cupcakes took 20 minutes to bake and 30 minutes to ice per batch. How long did it take Chelsea to make the cupcakes?"""
    # Define the time it takes to bake and ice a single batch of cupcakes
    BAKE_TIME = 20
    ICE_TIME = 30

    # Define the number of batches Chelsea made
    num_batches = 4

    # Calculate the total time it took to make the cupcakes
    total_time = (BAKE_TIME + ICE_TIME) * num_batches

    # Display the total time
    result = total_time
    return result

print(solution())