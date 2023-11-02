def solution():
    """John has a very inefficient toilet that uses 5 gallons of water per flush and his household flushed 15 times per day. He replaced it with a toilet that uses 80% less water per flush. How much water did John save in June?"""
    water_saved_per_flush = 5 * 0.8  # 80% reduction
    flushes_per_day = 15
    days_in_june = 30
    inefficient_toilet_water_use = 5 * flushes_per_day
    efficient_toilet_water_use = water_saved_per_flush * flushes_per_day
    water_saved_per_day = inefficient_toilet_water_use - efficient_toilet_water_use
    total_water_saved = water_saved_per_day * days_in_june
    result = total_water_saved
    return result

print(solution())