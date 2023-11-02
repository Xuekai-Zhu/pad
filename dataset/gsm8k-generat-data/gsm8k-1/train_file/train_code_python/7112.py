def solution():
    """Darius has 5 buckets of water. One contains 11 ounces, one contains 13 ounces, one contains 12 ounces, one contains 16 ounces, and one contains 10 ounces. He pours the ten-ounce bucket into a bigger bucket, along with one of the other four. The total in the bigger bucket is now 23 ounces. He pours the remaining three buckets into a second large bucket. How many ounces does the second large bucket contain?"""
    buckets = [11, 13, 12, 16, 10]
    bigger_bucket = 23
    remaining_sum = sum(buckets) - 23 - 10
    result = remaining_sum
    return result

print(solution())