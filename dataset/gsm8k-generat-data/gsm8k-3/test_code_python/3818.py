def solution():
    """There were 672 balloons that were either green, blue, yellow, or red. They were divided into equal groups and then Anya took half of the yellow ones home. How many balloons did Anya take home?"""
    # Define the total number of balloons
    total_balloons = 672

    # Divide the balloons into equal groups
    equal_groups = total_balloons // 4

    # Find the number of yellow balloons in each group
    yellow_balloons_per_group = equal_groups // 6

    # Find the total number of yellow balloons Anya took home
    total_yellow_balloons = yellow_balloons_per_group * 3

    # Display the number of yellow balloons Anya took home
    result = total_yellow_balloons
    return result

print(solution())