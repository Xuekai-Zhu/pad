def solution():
    num_batches = 4
    bake_time = 20
    ice_time = 30

    # Calculate the total time spent baking
    total_bake_time = num_batches * bake_time

    # Calculate the total time spent icing
    total_ice_time = num_batches * ice_time

    # Calculate the total time spent making cupcakes
    total_time = total_bake_time + total_ice_time
    result = total_time
    return result

print(solution())