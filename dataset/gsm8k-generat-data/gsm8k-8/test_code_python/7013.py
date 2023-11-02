def solution():
    # Calculate the total amount of fluid that will leak over 12 hours
    fluid_leaked = 1.5 * 12

    # Calculate the size of the bucket needed to hold twice the amount of fluid leaked
    bucket_size = fluid_leaked * 2
    result = bucket_size
    return result

print(solution())