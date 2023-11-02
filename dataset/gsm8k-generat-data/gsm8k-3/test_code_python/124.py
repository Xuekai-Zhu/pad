def solution():
    """Joy is winding balls of yarn for her cat to play with. The first ball is half the size of the second ball. The third ball is three times as large as the first ball. She used 27 feet of yarn for the third ball. How many feet of yarn did she use for the second ball?"""
    # Define the size of the first ball
    first_ball = None

    # Define the size of the second ball
    second_ball = 2 * first_ball

    # Define the size of the third ball
    third_ball = 3 * first_ball

    # Use the amount of yarn used for the third ball to calculate the size of the first ball
    first_ball = 27 / 4

    # Calculate the amount of yarn used for the second ball
    second_ball_yarn = (second_ball / first_ball) * 27

    result = second_ball_yarn
    return result

print(solution())