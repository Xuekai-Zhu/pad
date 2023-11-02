def solution():
    # Define the number of rows and roses per row
    num_rows = 10
    roses_per_row = 20

    # Calculate the number of red roses in each row
    red_roses = roses_per_row / 2

    # Calculate the number of remaining roses after red and white
    remaining_roses = roses_per_row - red_roses
    white_roses = 3/5 * remaining_roses

    # Calculate the number of pink roses in each row
    pink_roses = remaining_roses - white_roses

    # Calculate the total number of pink roses in the garden
    total_pink_roses = num_rows * pink_roses
    result = total_pink_roses
    return result

print(solution())