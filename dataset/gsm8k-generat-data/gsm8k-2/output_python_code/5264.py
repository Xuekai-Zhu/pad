def solution():
    """Wendy works at a chocolate factory packing chocolates. She can package 2 dozen chocolates in 5 minutes. How many individual chocolates can she package in 4 hours?"""
    dozen_chocolates = 2
    minutes_per_dozen = 5
    chocolates_per_minute = dozen_chocolates * 12 / minutes_per_dozen
    minutes_per_hour = 60
    total_minutes = 4 * minutes_per_hour
    total_chocolates = total_minutes * chocolates_per_minute
    result = total_chocolates
    return result

print(solution())