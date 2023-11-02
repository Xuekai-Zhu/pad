def solution():
    bucket_size = 120  # Size of each bucket
    num_times_filled = 14  # Number of times the bathtub was filled
    num_buckets_removed = 3  # Number of buckets removed to get to desired level
    days_per_week = 7  # Number of days per week Oliver takes a bath

    # Calculate the total amount of water the bathtub can hold
    total_water = bucket_size * num_times_filled

    # Calculate the amount of water Oliver uses for each bath
    bath_water = total_water - (num_buckets_removed * bucket_size)

    # Calculate the total amount of water Oliver uses for his daily baths
    weekly_water = bath_water * days_per_week
    result = weekly_water
    return result

print(solution())