def solution():
    # Define the number of buckets each person carries
    eden_buckets = 4
    mary_buckets = eden_buckets + 3
    iris_buckets = mary_buckets - 1

    # Calculate the total number of buckets
    total_buckets = eden_buckets + mary_buckets + iris_buckets

    # Calculate the total weight of sand
    sand_weight = total_buckets * 2

    result = sand_weight
    return result

print(solution())