def solution():
    
    # Define the number of holes dug each day
    day1_holes = 10
    day2_holes = 13
    day3_holes = 8

    # Calculate the total number of holes after the first three days
    total_holes = day1_holes + day2_holes + day3_holes

    # Calculate the number of holes left after the fourth day
    remaining_holes = total_holes - 1

    # Calculate the number of holes at the end of the fourth day
    fourth_day_holes = 4 * remaining_holes

    # Calculate the total number of holes after the fourth day
    total_holes += fourth_day_holes

    # Display the total number of holes at the end of the fourth day
    result = total_holes
    return result

print(solution())