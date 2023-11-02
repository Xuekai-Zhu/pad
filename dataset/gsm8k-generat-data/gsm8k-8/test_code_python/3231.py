def solution():
    # Define the total number of bread pieces Lucca bought
    total_bread = 200

    # Calculate the number of bread pieces Lucca ate on the first day
    day1_bread = total_bread * 1/4

    # Calculate the remaining bread pieces after Lucca ate on the first day
    remaining_bread = total_bread - day1_bread

    # Calculate the number of bread pieces Lucca ate on the second day
    day2_bread = remaining_bread * 2/5

    # Calculate the remaining bread pieces after Lucca ate on the second day
    remaining_bread = remaining_bread - day2_bread

    # Calculate the number of bread pieces Lucca ate on the third day
    day3_bread = remaining_bread * 1/2

    # Calculate the remaining bread pieces after Lucca ate on the third day
    remaining_bread = remaining_bread - day3_bread

    result = remaining_bread
    return result

print(solution())