def solution():
    """Lemuel is a basketball player. In one of the games, he made 2-point shots 7 times. He also made 3-points shots thrice. How many points, in total, did he make in that game?"""
    # Define the point value for each type of shot
    TWO_POINTS = 2
    THREE_POINTS = 3

    # Calculate the total points scored
    total_points = (7 * TWO_POINTS) + (3 * THREE_POINTS)

    # Display the total points scored
    result = total_points
    return result

print(solution())