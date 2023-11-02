def solution():
    """In his company, Kenzo has 80 office chairs with five legs each and 20 round tables with three legs each. If after a month 40% of the chairs are damaged and have to be disposed of, calculate the total number of legs of furniture Kenzo has remaining in his company."""
    # Define the number of office chairs, legs per chair, and number of round tables, legs per table
    num_chairs = 80
    chair_legs = 5
    num_tables = 20
    table_legs = 3

    # Calculate the total number of legs before any chairs are disposed of
    total_legs = num_chairs * chair_legs + num_tables * table_legs

    # Calculate the number of chairs that are disposed of
    num_disposed_chairs = int(num_chairs * 0.4)

    # Calculate the new number of chairs and total number of legs after disposing of some chairs
    num_chairs = num_chairs - num_disposed_chairs
    total_legs = num_chairs * chair_legs + num_tables * table_legs

    result = total_legs
    return result

print(solution())