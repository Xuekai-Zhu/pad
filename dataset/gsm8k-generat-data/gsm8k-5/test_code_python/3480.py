def solution():
    batches = 4  # Chelsea made 4 batches of cupcakes
    baking_time = 20  # It takes 20 minutes to bake one batch of cupcakes
    icing_time = 30  # It takes 30 minutes to ice one batch of cupcakes

    # Calculate the total time Chelsea spent baking and icing the cupcakes
    total_time = (baking_time + icing_time) * batches
    result = total_time
    return result

print(solution())