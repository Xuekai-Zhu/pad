def solution():
    """There are three buckets full of oranges. There are 22 oranges in the first bucket, 17 more oranges in the second bucket and 11 fewer oranges in the third bucket than in the second. How many oranges are there in all the buckets?"""
    first_bucket = 22
    second_bucket = first_bucket + 17
    third_bucket = second_bucket - 11
    all_buckets = first_bucket + second_bucket + third_bucket
    result = all_buckets
    return result

print(solution())