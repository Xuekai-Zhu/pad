def solution():
    # Define the bucket sizes
    bucket1 = 11
    bucket2 = 13
    bucket3 = 12
    bucket4 = 16
    bucket5 = 10

    # Find the two smaller buckets that add up to 23 ounces
    for bucket in [bucket1, bucket2, bucket3, bucket4]:
        if (23 - bucket) in [bucket1, bucket2, bucket3, bucket4] and (23 - bucket) != bucket:
            small_bucket1 = bucket
            small_bucket2 = 23 - bucket
            break

    # Calculate the total amount of water in the second large bucket
    second_bucket = small_bucket1 + small_bucket2 + bucket5
    return second_bucket

print(solution())