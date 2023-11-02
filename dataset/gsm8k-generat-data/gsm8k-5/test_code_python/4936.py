def solution():
    # Fill the 5-liter bucket
    bucket_5 = 5

    # Pour as much as possible into the 3-liter bucket
    bucket_3 = 3 if bucket_5 >= 3 else bucket_5

    # Pour the remaining into the 6-liter bucket
    bucket_6 = bucket_5 - bucket_3

    # Check if the 6-liter bucket is full
    if bucket_6 == 6:
        return 0  # The 6-liter bucket is already full, cannot add more water.

    # Calculate how much more water can be added to the 6-liter bucket
    remaining_capacity = 6 - bucket_6
    result = remaining_capacity
    return result

print(solution())