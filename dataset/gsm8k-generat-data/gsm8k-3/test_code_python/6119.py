def solution():
    """Peter has four horses. Each one eats 4 pounds of oats, twice a day, and 3 pounds of grain once a day. How many pounds of food does he need to feed his horses for 3 days?"""
    # Define the number of horses Peter has and their daily food requirements
    NUM_HORSES = 4
    OATS_PER_HORSE_PER_MEAL = 4
    GRAIN_PER_HORSE_PER_DAY = 3
    NUM_MEALS_PER_DAY = 3

    # Calculate the total amount of oats needed for 3 days
    total_oats = NUM_HORSES * OATS_PER_HORSE_PER_MEAL * NUM_MEALS_PER_DAY * 3

    # Calculate the total amount of grain needed for 3 days
    total_grain = NUM_HORSES * GRAIN_PER_HORSE_PER_DAY * 3

    # Calculate the total amount of food needed for 3 days
    total_food = total_oats + total_grain

    # Display the total amount of food needed
    result = total_food
    return result

print(solution())