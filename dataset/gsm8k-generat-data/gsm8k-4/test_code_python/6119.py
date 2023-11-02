def solution():
    """Peter has four horses. Each one eats 4 pounds of oats, twice a day, and 3 pounds of grain once a day. How many pounds of food does he need to feed his horses for 3 days?"""
    # Define the number of horses, the amount of oats they eat per meal, and the amount of grain they eat per day
    num_horses = 4
    oats_per_meal = 4
    grain_per_day = 3

    # Calculate the total amount of oats and grain each horse needs per day
    oats_per_day = oats_per_meal * 2
    grain_per_horse_per_day = grain_per_day

    # Calculate the total amount of oats and grain needed for all horses for 3 days
    total_oats = oats_per_day * num_horses * 3
    total_grain = grain_per_horse_per_day * num_horses * 3

    # Calculate the total amount of food needed for all horses for 3 days
    total_food = total_oats + total_grain

    # Return the result
    result = total_food
    return result

print(solution())