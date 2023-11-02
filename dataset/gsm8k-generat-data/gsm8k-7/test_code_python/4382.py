def solution():
    num_rows = 10
    num_roses_per_row = 20

    # Calculate the total number of roses in the garden
    total_roses = num_rows * num_roses_per_row

    # Calculate the number of red roses
    num_red_roses = (1 / 2) * total_roses

    # Calculate the number of remaining roses after accounting for the red roses
    remaining_roses = total_roses - num_red_roses

    # Calculate the number of white roses
    num_white_roses = (3 / 5) * remaining_roses

    # Calculate the number of pink roses
    num_pink_roses = remaining_roses - num_white_roses

    result = num_pink_roses
    return result

print(solution())