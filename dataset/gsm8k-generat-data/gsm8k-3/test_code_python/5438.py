def solution():
    """Elena has 8 lilies and 5 tulips in her garden. Each lily has 6 petals. Each tulip has 3 petals. How many flower petals are in Elena’s garden?"""
    # Define the number of lilies and tulips in Elena's garden
    lilies = 8
    tulips = 5

    # Define the number of petals on each lily and tulip
    lily_petals = 6
    tulip_petals = 3

    # Calculate the total number of petals in Elena's garden
    total_petals = (lilies * lily_petals) + (tulips * tulip_petals)

    # Display the total number of petals
    result = total_petals
    return result

print(solution())