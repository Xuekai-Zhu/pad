def solution():
    # Calculate the total number of guests
    total_guests = 22 + 36

    # Calculate the total number of flags needed
    total_flags = total_guests + 2

    # Calculate the number of $1.00 flag bundles needed
    flag_bundles = total_flags // 5

    # Calculate the total cost of the flags
    flag_cost = flag_bundles * 1.00

    result = flag_cost
    return result

print(solution())