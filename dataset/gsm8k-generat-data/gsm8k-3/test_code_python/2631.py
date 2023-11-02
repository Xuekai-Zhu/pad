def solution():
    """Jenson and Kingsley have a tailoring business. Jenson makes 3 shirts, and Kingsley makes 5 pairs of pants per day. If each shirt uses 2 yards of fabric and a pair of pants uses 5 yards of fabric, how many yards of fabric do they need every 3 days?"""
    # Define the number of shirts and pairs of pants made per day
    SHIRTS_PER_DAY = 3
    PANTS_PER_DAY = 5

    # Define the number of yards of fabric used for each shirt and pair of pants
    SHIRT_FABRIC = 2
    PANTS_FABRIC = 5

    # Calculate the total yards of fabric used per day
    fabric_per_day = (SHIRTS_PER_DAY * SHIRT_FABRIC) + (PANTS_PER_DAY * PANTS_FABRIC)

    # Calculate the total yards of fabric needed for 3 days
    fabric_per_3_days = fabric_per_day * 3

    # Display the total yards of fabric needed
    result = fabric_per_3_days
    return result

print(solution())