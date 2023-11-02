def solution():
    """Billy has four horses. Each one eats 4 pounds of oats, twice a day. How many pounds of oats does he need to feed his horses for 3 days?"""
    # Define the number of horses and the amount of oats per horse per feeding
    NUM_HORSES = 4
    OATS_PER_HORSE = 4

    # Define the number of feedings per day and the number of days
    NUM_FEEDINGS_PER_DAY = 2
    NUM_DAYS = 3

    # Calculate the total amount of oats needed
    total_oats = NUM_HORSES * OATS_PER_HORSE * NUM_FEEDINGS_PER_DAY * NUM_DAYS

    # Display the total amount of oats needed
    result = total_oats
    return result

print(solution())