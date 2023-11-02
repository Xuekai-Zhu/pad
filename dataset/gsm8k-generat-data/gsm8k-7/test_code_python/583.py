def solution():
    largest_rate = 3
    medium_rate = largest_rate / 2
    smallest_rate = medium_rate / 3
    time_period = 120  # 2 hours in minutes

    # Calculate the total amount of water leaked by the largest hole
    total_largest_leak = largest_rate * time_period

    # Calculate the total amount of water leaked by the medium-sized hole
    total_medium_leak = medium_rate * time_period

    # Calculate the total amount of water leaked by the smallest hole
    total_smallest_leak = smallest_rate * time_period

    # Calculate the combined amount of water leaked from all three holes
    total_leak = total_largest_leak + total_medium_leak + total_smallest_leak
    result = total_leak
    return result

print(solution())