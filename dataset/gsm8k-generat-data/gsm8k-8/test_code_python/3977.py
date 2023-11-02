def solution():
    # Define number of sequins in each row
    blue_sequins = 8
    purple_sequins = 12
    green_sequins = 6

    # Define number of rows for each color
    blue_rows = 6
    purple_rows = 5
    green_rows = 9

    # Calculate total number of sequins
    total_sequins = (blue_sequins * blue_rows) + (purple_sequins * purple_rows) + (green_sequins * green_rows)
    result = total_sequins
    return result

print(solution())