def solution():
    """Hamza has several empty buckets of different sizes, holding either 3, 5, or 6 liters. She fills the 5-liter bucket and pours as much as she can into the 3-liter bucket. Then, she pours the remainder into the 6-liter bucket. How much more water, in liters, can she put into the 6-liter bucket, without overflowing?"""
    bucket_sizes = [3, 5, 6]
    bucket_states = [0, 0, 0]  # initialize the buckets to be empty
    # fill the 5-liter bucket
    bucket_states[1] = 5
    # pour into the 3-liter bucket (it can hold 3 liters maximum)
    amount_poured = min(bucket_states[1], bucket_sizes[0]-bucket_states[0])
    bucket_states[1] -= amount_poured
    bucket_states[0] += amount_poured
    # pour remaining water from 5-liter bucket into 6-liter bucket
    amount_poured = min(bucket_states[1], bucket_sizes[2]-bucket_states[2])
    bucket_states[1] -= amount_poured
    bucket_states[2] += amount_poured
    # calculate how much more water can be put into the 6-liter bucket without overflowing
    max_amount = bucket_sizes[2] - bucket_states[2]
    result = max_amount
    return result

print(solution())