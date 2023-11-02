def solution():
    # Define the number of kangaroos and goats
    kangaroos = 23
    goats = 3 * kangaroos

    # Calculate the number of legs
    kangaroo_legs = 2 * kangaroos
    goat_legs = 4 * goats
    total_legs = kangaroo_legs + goat_legs
    result = total_legs
    return result

print(solution())