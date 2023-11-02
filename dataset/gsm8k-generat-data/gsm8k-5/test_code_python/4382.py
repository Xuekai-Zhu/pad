def solution():
    roses_per_row = 20  # There are 20 roses in each row
    total_rows = 10  # There are 10 rows in Mrs. Dawson's rose garden

    # Calculate the total number of red roses
    red_roses = (roses_per_row / 2) * total_rows

    # Calculate the remaining roses after the red ones
    remaining_roses = (roses_per_row / 2) * total_rows

    # Calculate the number of white roses after the red ones
    white_roses = (3/5) * remaining_roses

    # Calculate the number of pink roses
    pink_roses = remaining_roses - white_roses

    result = pink_roses
    return result

print(solution())