def solution():
    largest_leak_rate = 3  # Largest hole leaks water at 3 ounces per minute
    medium_leak_rate = largest_leak_rate / 2  # Medium-sized hole leaks water at half the rate of the largest hole
    smallest_leak_rate = medium_leak_rate / 3  # Smallest hole leaks water at one-third the rate of the medium-sized hole
    time_in_minutes = 2 * 60  # 2-hour time period in minutes

    # Total amount of water leaked from all three holes
    total_leak = (largest_leak_rate + medium_leak_rate + smallest_leak_rate) * time_in_minutes
    result = total_leak
    return result

print(solution())