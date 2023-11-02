def solution():
    """Grace is looking to plant some lettuce in her raised bed garden. Her raised bed is comprised of 2 large beds on top with 2 medium beds on the bottom. The top bed can hold 4 rows of lettuce with 25 seeds being sown per row. The medium bed can house 3 rows with 20 seeds being sown per row. How many seeds can Grace plant in all four beds of her raised bed garden?"""
    top_bed_rows = 4
    top_bed_seeds_per_row = 25
    medium_bed_rows = 3
    medium_bed_seeds_per_row = 20
    top_bed_capacity = top_bed_rows * top_bed_seeds_per_row
    medium_bed_capacity = medium_bed_rows * medium_bed_seeds_per_row
    total_capacity = 2 * top_bed_capacity + 2 * medium_bed_capacity
    result = total_capacity
    return result

print(solution())