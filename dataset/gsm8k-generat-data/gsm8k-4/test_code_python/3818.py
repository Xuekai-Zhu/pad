def solution():
    """There were 672 balloons that were either green, blue, yellow, or red. They were divided into equal groups and then Anya took half of the yellow ones home. How many balloons did Anya take home?"""
    # Define the total number of balloons
    total_balloons = 672

    # Define the number of colors of balloons
    num_colors = 4

    # Calculate the number of balloons per color
    balloons_per_color = total_balloons / num_colors

    # Calculate the number of yellow balloons
    yellow_balloons = balloons_per_color

    # Calculate the number of yellow balloons Anya took home
    anya_balloons = yellow_balloons / 2

    # Return the result
    result = anya_balloons
    return result

print(solution())