def solution():
    # Calculate the total number of apartments
    total_apartments = 2 * 12 * 6  # Two buildings, each with 12 floors with 6 apartments each

    # Calculate the total number of doors needed
    doors_per_apartment = 7  # Each apartment needs 7 doors
    total_doors = total_apartments * doors_per_apartment

    result = total_doors
    return result

print(solution())