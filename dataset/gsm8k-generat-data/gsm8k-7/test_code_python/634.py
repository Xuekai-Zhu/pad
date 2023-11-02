def solution():
    num_hats_3_stripes = 4
    num_stripes_3_stripes = 3

    num_hats_4_stripes = 3
    num_stripes_4_stripes = 4

    num_hats_no_stripes = 6
    num_stripes_no_stripes = 0

    num_hats_5_stripes = 2
    num_stripes_5_stripes = 5

    # Calculate the total number of stripes on hats with 3 stripes
    total_stripes_3_stripes = num_hats_3_stripes * num_stripes_3_stripes

    # Calculate the total number of stripes on hats with 4 stripes
    total_stripes_4_stripes = num_hats_4_stripes * num_stripes_4_stripes

    # Calculate the total number of stripes on hats with no stripes
    total_stripes_no_stripes = num_hats_no_stripes * num_stripes_no_stripes

    # Calculate the total number of stripes on hats with 5 stripes
    total_stripes_5_stripes = num_hats_5_stripes * num_stripes_5_stripes

    # Calculate the combined total number of stripes on all hats
    combined_total_stripes = total_stripes_3_stripes + total_stripes_4_stripes + total_stripes_no_stripes + total_stripes_5_stripes
    result = combined_total_stripes
    return result

print(solution())