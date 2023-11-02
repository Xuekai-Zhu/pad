def solution():
    total_balloons = 672  # There were 672 balloons in total
    num_colors = 4  # There were 4 different colors of balloons
    equal_groups = total_balloons / num_colors  # Divide the balloons into equal groups

    # Calculate how many yellow balloons Anya took home
    yellow_balloons = equal_groups / 2

    result = yellow_balloons
    return result

print(solution())