def solution():
    """In his company, Kenzo has 80 office chairs with five legs each and 20 round tables with three legs each. If after a month 40% of the chairs are damaged and have to be disposed of, calculate the total number of legs of furniture Kenzo has remaining in his company."""
    # Define the number of legs for each type of furniture
    CHAIR_LEGS = 5
    TABLE_LEGS = 3

    # Define the initial numbers of chairs and tables
    num_chairs = 80
    num_tables = 20

    # Calculate the total number of legs before any chairs are disposed of
    total_legs = num_chairs * CHAIR_LEGS + num_tables * TABLE_LEGS

    # Calculate the number of chairs that need to be disposed of
    num_disposed_chairs = round(0.4 * num_chairs)

    # Calculate the new total number of legs after chairs are disposed of
    new_num_chairs = num_chairs - num_disposed_chairs
    new_total_legs = new_num_chairs * CHAIR_LEGS + num_tables * TABLE_LEGS

    # Display the new total number of legs
    result = new_total_legs
    return result

print(solution())