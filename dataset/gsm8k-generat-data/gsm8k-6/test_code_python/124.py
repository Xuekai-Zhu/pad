def solution():
    # Find the amount of yarn Joy used for the first ball
    first_ball = 27 / (3*2 + 1)  # the third ball is three times as large as the first ball, and there are three balls in total

    # Find the amount of yarn Joy used for the second ball
    second_ball = 2 * first_ball  # the second ball is twice the size of the first ball
    result = second_ball
    return result

print(solution())