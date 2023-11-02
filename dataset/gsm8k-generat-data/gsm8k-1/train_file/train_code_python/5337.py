def solution():
    """Rick can iron 4 dress shirts in an hour. He can iron 3 dress pants in an hour. If he spends 3 hours ironing dress shirts and 5 hours ironing dress pants, how many pieces of clothing has he ironed?"""
    shirts_per_hour = 4
    pants_per_hour = 3
    hours_shirts = 3
    hours_pants = 5
    total_shirts = shirts_per_hour * hours_shirts
    total_pants = pants_per_hour * hours_pants
    total_clothing = total_shirts + total_pants
    result = total_clothing
    return result

print(solution())