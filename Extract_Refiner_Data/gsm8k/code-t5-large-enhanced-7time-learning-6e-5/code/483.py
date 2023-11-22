def solution():
    
    # Define the number of horses and the amount of oats they consume per meal
    NUM_HORSES = 4
    OATS_PER_MEAL = 5

    # Define the number of meals he feeds his horses per day
    NUM_MEALS_PER_DAY = 2

    # Define the number of days he needs to feed his horses
    NUM_DAYS = 5

    # Calculate the total amount of oats he needs for 5 days
    total_oats = NUM_HORSES * OATS_PER_MEAL * NUM_MEALS_PER_DAY * NUM_DAYS

    # Calculate the number of bags of oats he needs to feed his horses
    bags_of_oats = total_oats / 50

    # Display the number of bags of oats
    result = bags_of_oats
    return result

print(solution())