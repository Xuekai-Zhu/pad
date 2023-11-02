def solution():
    third_ball_yarn = 27
    third_ball_size = 3
    first_ball_size = 0.5

    # Calculate the size of the first ball
    first_ball_yarn = third_ball_yarn / (third_ball_size * first_ball_size)

    # Calculate the size of the second ball (twice the size of the first ball)
    second_ball_size = 2 * first_ball_size

    # Calculate the amount of yarn used for the second ball
    second_ball_yarn = second_ball_size * (third_ball_yarn / third_ball_size)

    result = second_ball_yarn
    return result

print(solution())