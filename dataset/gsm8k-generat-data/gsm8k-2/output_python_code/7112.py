def solution():
    """Darius has 5 buckets of water. One contains 11 ounces, one contains 13 ounces, one contains 12 ounces, one contains 16 ounces, and one contains 10 ounces. He pours the ten-ounce bucket into a bigger bucket, along with one of the other four. The total in the bigger bucket is now 23 ounces. He pours the remaining three buckets into a second large bucket. How many ounces does the second large bucket contain?"""
    buckets = [11, 13, 12, 16, 10]
    bigger_bucket = 23 - 10
    for bucket in buckets:
        if bucket != 10:
            if bucket + 10 == bigger_bucket:
                smaller_bucket_total = sum(buckets) - bucket - 10
                second_large_bucket = smaller_bucket_total
    result = second_large_bucket
    return result

print(solution())