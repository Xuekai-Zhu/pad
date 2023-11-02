def solution():
    """Joy is winding balls of yarn for her cat to play with. The first ball is half the size of the second ball. The third ball is three times as large as the first ball. She used 27 feet of yarn for the third ball. How many feet of yarn did she use for the second ball?"""
    third_ball_size = 27
    first_ball_size = third_ball_size / 3
    second_ball_size = 2 * first_ball_size
    second_ball_yarn = (4/3) * (second_ball_size**3) * 3.14 * 1.2
    result = second_ball_yarn
    return result

print(solution())