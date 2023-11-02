def solution():
    """There are three buckets full of oranges. There are 22 oranges in the first bucket, 17 more oranges in the second bucket and 11 fewer oranges in the third bucket than in the second. How many oranges are there in all the buckets?"""
    oranges_bucket1 = 22
    oranges_bucket2 = oranges_bucket1 + 17
    oranges_bucket3 = oranges_bucket2 - 11
    total_oranges = oranges_bucket1 + oranges_bucket2 + oranges_bucket3
    result = total_oranges
    return result

print(solution())