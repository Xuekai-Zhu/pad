def solution():
    """Billy has four horses. Each one eats 4 pounds of oats, twice a day. How many pounds of oats does he need to feed his horses for 3 days?"""
    # Define the number of horses and the amount of oats they eat per day
    num_horses = 4
    oats_per_horse_per_day = 4 * 2

    # Calculate the total amount of oats needed for 3 days
    total_oats = num_horses * oats_per_horse_per_day * 3

    # Return the result
    result = total_oats
    return result

print(solution())