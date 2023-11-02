def solution():
    """Rick can iron 4 dress shirts in an hour.  He can iron 3 dress pants in an hour.  If he spends 3 hours ironing dress shirts and 5 hours ironing dress pants, how many pieces of clothing has he ironed?"""
    # Define the number of dress shirts ironed per hour
    SHIRTS_PER_HOUR = 4

    # Define the number of dress pants ironed per hour
    PANTS_PER_HOUR = 3

    # Calculate the number of dress shirts ironed
    shirts_ironed = SHIRTS_PER_HOUR * 3

    # Calculate the number of dress pants ironed
    pants_ironed = PANTS_PER_HOUR * 5

    # Add the number of dress shirts and dress pants to get the total number of pieces of clothing ironed
    total_ironed = shirts_ironed + pants_ironed

    # Display the total number of pieces of clothing ironed
    result = total_ironed
    return result

print(solution())