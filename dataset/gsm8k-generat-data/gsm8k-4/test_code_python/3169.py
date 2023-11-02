def solution():
    """John cuts his grass to 2 inches. It grows .5 inches per month. When it gets to 4 inches he cuts it back down to 2 inches. It cost $100 to get his grass cut. How much does he pay per year?"""
    # Define the growth rate of the grass
    growth_rate = 0.5

    # Define the target height of the grass
    target_height = 4

    # Define the cost of cutting the grass
    cutting_cost = 100

    # Calculate the time it takes for the grass to grow to the target height
    time_to_target = (target_height - 2) / growth_rate

    # Calculate the number of times John needs to cut the grass in a year
    cut_times_per_year = 12 / time_to_target

    # Calculate the cost of cutting the grass per year
    cost_per_year = cutting_cost * cut_times_per_year

    result = cost_per_year
    return result

print(solution())