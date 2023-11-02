def solution():
    """Gunther needs to clean his apartment. It takes him 45 minutes to vacuum the carpets, 60 minutes to dust the furniture, 30 minutes to mop the floors in his kitchen, and 5 minutes to brush each cat, and he has three cats. If he has 3 hours of free time available, and he uses this time to clean his apartment, how many minutes of free time will he have left after he cleans the apartment?"""
    # Define the time taken for each cleaning task
    vacuum_time = 45
    dust_time = 60
    mop_time = 30
    cat_brush_time = 5

    # Calculate the total time to clean the apartment
    total_time = vacuum_time + dust_time + mop_time + (cat_brush_time * 3)

    # Convert the free time available to minutes
    free_time = 3 * 60

    # Calculate the remaining free time after cleaning the apartment
    remaining_time = free_time - total_time

    result = remaining_time
    return result

print(solution())