def solution():
    """Jane is sewing sequins onto her trapeze artist costume. She sews 6 rows of 8 blue sequins each, 5 rows of 12 purple sequins each, and 9 rows of 6 green sequins each. How many sequins does she add total?"""
    # Define the number of sequins in each row of each color
    BLUE_SEQUINS = 8
    PURPLE_SEQUINS = 12
    GREEN_SEQUINS = 6

    # Define the number of rows of each color
    blue_rows = 6
    purple_rows = 5
    green_rows = 9

    # Calculate the total number of blue sequins
    blue_sequins = blue_rows * BLUE_SEQUINS

    # Calculate the total number of purple sequins
    purple_sequins = purple_rows * PURPLE_SEQUINS

    # Calculate the total number of green sequins
    green_sequins = green_rows * GREEN_SEQUINS

    # Calculate the total number of sequins added
    total_sequins = blue_sequins + purple_sequins + green_sequins

    # Display the total number of sequins
    result = total_sequins
    return result

print(solution())