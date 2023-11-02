def solution():
    """Grace is looking to plant some lettuce in her raised bed garden. Her raised bed is comprised of 2 large beds on top with 2 medium beds on the bottom. The top bed can hold 4 rows of lettuce with 25 seeds being sown per row. The medium bed can house 3 rows with 20 seeds being sown per row. How many seeds can Grace plant in all four beds of her raised bed garden?"""
    # Define the number of seeds per row for each bed
    top_seeds_per_row = 25
    medium_seeds_per_row = 20

    # Calculate the total number of seeds that can be planted in the top bed
    top_rows = 4
    top_seeds = top_rows * top_seeds_per_row

    # Calculate the total number of seeds that can be planted in the medium bed
    medium_rows = 3
    medium_seeds = medium_rows * medium_seeds_per_row

    # Calculate the total number of seeds that can be planted in all four beds
    total_seeds = (top_seeds * 2) + (medium_seeds * 2)

    result = total_seeds
    return result

print(solution())