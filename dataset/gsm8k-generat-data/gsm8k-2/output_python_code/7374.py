def solution():
    """Carlos is doing his laundry. He needs to wash two loads, which takes 45 minutes per load. Then he can combine both loads and dry them, which takes 75 minutes. How long does his laundry take in total?"""
    wash_time_per_load = 45
    dry_time_combined_load = 75
    total_laundry_time = (wash_time_per_load * 2) + dry_time_combined_load
    result = total_laundry_time
    return result

print(solution())