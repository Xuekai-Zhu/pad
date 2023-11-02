def solution():
    # Calculate the amount of fluid that will leak over 12 hours
    leaked_fluid = 1.5 * 12

    # Calculate the size of the bucket needed to hold twice the amount of leaked fluid
    bucket_size = leaked_fluid * 2
    result = bucket_size
    return result

print(solution())