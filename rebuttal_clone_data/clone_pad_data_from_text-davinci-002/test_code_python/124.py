def solution():
    """Joy is winding balls of yarn for her cat to play with. The first ball is half the size of the second ball. The third ball is three times as large as the first ball. She used 27 feet of yarn for the third ball. How many feet of yarn did she use for the second ball?"""
    size_first_ball = 1/2
    size_second_ball = 1
    size_third_ball = 3
    yarn_third_ball = 27
    yarn_second_ball = yarn_third_ball / size_third_ball * size_second_ball
    result = yarn_second_ball
    return result

print(solution())