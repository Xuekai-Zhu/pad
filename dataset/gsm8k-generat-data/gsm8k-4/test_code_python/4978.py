def solution():
    """Bob is going to plant corn in part of his garden. The rows are 120 feet long, and each seed needs its own dedicated space of 18 inches to its right. How many seeds can Bob plant in each row?"""
    # Define the length of the rows in feet and inches
    ROW_LENGTH_FEET = 120
    ROW_LENGTH_INCHES = ROW_LENGTH_FEET * 12

    # Define the space needed for each seed in inches
    SEED_SPACE_INCHES = 18

    # Calculate the number of spaces available for seeds
    seed_spaces = ROW_LENGTH_INCHES / SEED_SPACE_INCHES

    # Round down to get the integer number of seeds that can fit in each row
    seeds_per_row = int(seed_spaces)

    # return the result
    result = seeds_per_row
    return result

print(solution())