def solution():
    """Carlos is doing his laundry. He needs to wash two loads, which takes 45 minutes per load. Then he can combine both loads and dry them, which takes 75 minutes. How long does his laundry take in total?"""
    wash_time_per_load = 45
    total_wash_time = wash_time_per_load * 2
    dry_time = 75
    total_time = total_wash_time + dry_time
    result = total_time
    return result

print(solution())