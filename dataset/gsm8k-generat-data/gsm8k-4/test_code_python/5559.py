def solution():
    """Lemuel is a basketball player. In one of the games, he made 2-point shots 7 times. He also made 3-points shots thrice. How many points, in total, did he make in that game?"""
    # Define the number of 2-point shots and 3-point shots
    num_2point = 7
    num_3point = 3

    # Calculate the total points made
    total_points = num_2point*2 + num_3point*3

    # return the result
    result = total_points
    return result

print(solution())