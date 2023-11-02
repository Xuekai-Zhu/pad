def solution():
    blue_rows = 6
    blue_sequins_per_row = 8

    purple_rows = 5
    purple_sequins_per_row = 12

    green_rows = 9
    green_sequins_per_row = 6

    # Calculate the total number of blue sequins
    blue_total = blue_rows * blue_sequins_per_row

    # Calculate the total number of purple sequins
    purple_total = purple_rows * purple_sequins_per_row

    # Calculate the total number of green sequins
    green_total = green_rows * green_sequins_per_row

    # Calculate the total number of sequins Jane adds in total
    total_sequins = blue_total + purple_total + green_total
    result = total_sequins
    return result

print(solution())