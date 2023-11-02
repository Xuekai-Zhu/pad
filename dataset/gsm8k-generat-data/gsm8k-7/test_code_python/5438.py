def solution():
    num_lilies = 8
    num_tulips = 5
    lily_petals = 6
    tulip_petals = 3

    # Calculate the total number of petals from all lilies
    total_lily_petals = num_lilies * lily_petals

    # Calculate the total number of petals from all tulips
    total_tulip_petals = num_tulips * tulip_petals

    # Calculate the total number of flower petals in Elena's garden
    total_petals = total_lily_petals + total_tulip_petals
    result = total_petals
    return result

print(solution())