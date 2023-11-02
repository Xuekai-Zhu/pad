def solution():
    bucket_size = 120  # Oliver's bucket holds 120 ounces of water
    num_buckets_filled = 14  # Oliver filled the bathtub 14 times
    num_buckets_removed = 3  # Oliver removed 3 buckets to get to his desired water level
    water_per_fill = bucket_size * num_buckets_filled  # Total water used to fill the tub
    water_per_bath = water_per_fill - (bucket_size * num_buckets_removed)  # Water used per bath
    water_per_week = water_per_bath * 7  # Water used per week (assuming daily baths)
    result = water_per_week
    return result

print(solution())