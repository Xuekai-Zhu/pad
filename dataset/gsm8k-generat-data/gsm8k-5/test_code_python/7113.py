def solution():
    buckets = [11, 13, 12, 16, 10]  # Darius has 5 buckets of water
    total = sum(buckets)  # Find the total amount of water in all buckets

    # Find the second larger bucket by subtracting the total in the first larger bucket from the total amount of water
    second_large_bucket = total - 23

    result = second_large_bucket
    return result

print(solution())