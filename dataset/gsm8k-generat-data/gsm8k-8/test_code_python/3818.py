def solution():
    # Define the total number of balloons
    total_balloons = 672

    # Divide the balloons into equal groups
    equal_groups = total_balloons // 4

    # Calculate the number of yellow balloons
    yellow_balloons = equal_groups

    # Calculate the number of balloons Anya took home
    balloons_taken_home = yellow_balloons // 2

    result = balloons_taken_home
    return result

print(solution())