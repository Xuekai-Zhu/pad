def solution():
    """Oliver wonders how much water his bathtub can hold. So he takes a bucket that holds 120 ounces and starts filling the bathtub. When it reaches the top, he sees that he filled it 14 times. Then he wonders how much bathwater he uses, so he starts taking away buckets until it gets to the level he puts it at. He needs to take away 3 buckets to do this. Finally, he wonders how much water he uses in a week for his baths, which he takes every day. How much water does he use each week?"""
    bucket_size = 120
    filled_buckets = 14
    removed_buckets = 3
    total_water = (filled_buckets - removed_buckets) * bucket_size
    water_per_week = total_water * 7
    result = water_per_week
    return result

print(solution())