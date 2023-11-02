def solution():
    total_balloons = 672
    num_groups = 4

    # Calculate the number of balloons in each group
    balloons_per_group = total_balloons / num_groups

    # Calculate the number of yellow balloons in each group
    yellow_balloons_per_group = balloons_per_group / 4

    # Calculate the total number of yellow balloons that Anya took home
    num_yellow_balloons = yellow_balloons_per_group * num_groups / 2

    result = num_yellow_balloons
    return result

print(solution())