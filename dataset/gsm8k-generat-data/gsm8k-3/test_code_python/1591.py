def solution():
    """There are 3414 yellow balloons and there are 1762 more black balloons than yellow balloons. If the balloons will be evenly divided among 10 schools, how many balloons will one school receive?"""
    # Define the number of yellow balloons and the difference in number between yellow and black balloons
    yellow_balloons = 3414
    black_balloons_diff = 1762

    # Calculate the total number of balloons
    total_balloons = yellow_balloons + (yellow_balloons + black_balloons_diff)

    # Calculate the number of balloons per school
    balloons_per_school = total_balloons / 10

    # Display the number of balloons per school
    result = balloons_per_school
    return result

print(solution())