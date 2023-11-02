def solution():
    """Hamza has several empty buckets of different sizes, holding either 3, 5, or 6 liters. She fills the 5-liter bucket and pours as much as she can into the 3-liter bucket. Then, she pours the remainder into the 6-liter bucket. How much more water, in liters, can she put into the 6-liter bucket, without overflowing?"""
    bucket_5 = 5
    bucket_3 = 3
    bucket_6 = 6
    water_poured = bucket_5 - bucket_3
    remaining_water = bucket_5 - water_poured
    space_left_in_6 = bucket_6 - remaining_water
    result = space_left_in_6
    return result

print(solution())