def solution():
    """Hamza has several empty buckets of different sizes, holding either 3, 5, or 6 liters. She fills
    the 5-liter bucket and pours as much as she can into the 3-liter bucket. Then, she pours the
    remainder into the 6-liter bucket. How much more water, in liters, can she put into the 6-liter bucket, without overflowing?"""
    # Define the capacities of the buckets
    bucket_3 = 0
    bucket_5 = 5
    bucket_6 = 0

    # Fill the 3-liter bucket with water from the 5-liter bucket
    while bucket_3 < 3:
        bucket_5 -= 1
        bucket_3 += 1

    # Pour the remaining water from the 5-liter bucket into the 6-liter bucket
    bucket_6 += bucket_5
    bucket_5 = 0

    # Check how much more water can be added to the 6-liter bucket
    remaining = 6 - bucket_6

    # return the result
    result = remaining
    return result

print(solution())