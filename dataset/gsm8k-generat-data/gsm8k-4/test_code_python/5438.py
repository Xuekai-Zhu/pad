def solution():
    """Elena has 8 lilies and 5 tulips in her garden. Each lily has 6 petals. Each tulip has 3 petals. How many flower petals are in Elena’s garden?"""
    # Define the number of lilies and tulips in Elena's garden
    num_lilies = 8
    num_tulips = 5

    # Calculate the total number of petals in the lilies and tulips
    total_lily_petals = num_lilies * 6
    total_tulip_petals = num_tulips * 3

    # Calculate the total number of flower petals
    total_petals = total_lily_petals + total_tulip_petals

    # return the result
    result = total_petals
    return result

print(solution())