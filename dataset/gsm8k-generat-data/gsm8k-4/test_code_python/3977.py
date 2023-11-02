def solution():
    """Jane is sewing sequins onto her trapeze artist costume. She sews 6 rows of 8 blue sequins each, 5 rows of 12 purple sequins each, and 9 rows of 6 green sequins each. How many sequins does she add total?"""
    # Define the number of sequins per row for each color
    blue_sequins_per_row = 8
    purple_sequins_per_row = 12
    green_sequins_per_row = 6

    # Calculate the total number of sequins for each color
    blue_sequins = 6 * blue_sequins_per_row
    purple_sequins = 5 * purple_sequins_per_row
    green_sequins = 9 * green_sequins_per_row

    # Calculate the total number of sequins Jane adds
    total_sequins = blue_sequins + purple_sequins + green_sequins

    # return the result
    result = total_sequins
    return result

print(solution())