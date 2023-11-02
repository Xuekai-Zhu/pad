def solution():
    """Hamza has several empty buckets of different sizes, holding either 3, 5, or 6 liters. She fills the 5-liter bucket and pours as much as she can into the 3-liter bucket. Then, she pours the remainder into the 6-liter bucket. How much more water, in liters, can she put into the 6-liter bucket, without overflowing?"""
    # Fill the 5-liter bucket
    bucket_5 = 5

    # Pour as much as possible into the 3-liter bucket
    bucket_3 = 3 if bucket_5 > 3 else bucket_5

    # Pour the remaining water into the 6-liter bucket
    bucket_6 = bucket_5 - bucket_3 if bucket_5 - bucket_3 < 6 else 6

    # Calculate how much more water can be put into the 6-liter bucket
    remaining = 6 - bucket_6

    # Display the remaining water
    result = remaining
    return result

print(solution())