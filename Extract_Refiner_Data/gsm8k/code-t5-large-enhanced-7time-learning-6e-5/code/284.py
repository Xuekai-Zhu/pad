def solution():
    
    # Define the weight of each flagstone and the total weight of the trip
    FLAGSTONE_WEIGHT = 75
    TRICK_WEIGHT = 2000

    # Calculate the total weight of the flagstones
    total_weight = 80 * FLAGSTONE_WEIGHT

    # Calculate the number of trucks needed to transport the flagstones
    trucks_needed = total_weight // TRICK_WEIGHT

    # If the total weight is not evenly divisible by the truck weight, add one more trip
    if total_weight % TRICK_WEIGHT!= 0:
        trucks_needed += 1

    # Display the number of trucks needed
    result = trucks_needed
    return result

print(solution())