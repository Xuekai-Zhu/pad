def solution():
    # Calculate the number of balloons in each group
    num_groups = 4  # there are 4 colors of balloons
    total_balloons = 672
    balloons_per_group = total_balloons // num_groups

    # Calculate the number of yellow balloons Anya took home
    num_yellow = balloons_per_group
    num_yellow_half = num_yellow // 2
    result = num_yellow_half
    return result

print(solution())