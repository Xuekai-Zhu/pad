def solution():
    """Joy is winding balls of yarn for her cat to play with. The first ball is half the size of the second ball. The third ball is three times as large as the first ball. She used 27 feet of yarn for the third ball. How many feet of yarn did she use for the second ball?"""
    # Define the size of the first ball in terms of the second ball
    first_ball_size = 0.5

    # Define the size of the third ball in terms of the second ball
    third_ball_size = 3 * first_ball_size

    # Calculate the total amount of yarn used for all three balls
    total_yarn = 27

    # Calculate the amount of yarn used for the first ball
    first_ball_yarn = total_yarn / (first_ball_size + 1 + third_ball_size)

    # Calculate the amount of yarn used for the second ball
    second_ball_yarn = first_ball_yarn * 2

    # Return the result
    result = second_ball_yarn
    return result

print(solution())