def solution():
    """Joy is winding balls of yarn for her cat to play with. The first ball is half the size of the second ball. The third ball is three times as large as the first ball. She used 27 feet of yarn for the third ball. How many feet of yarn did she use for the second ball?"""
    third_ball = 27
    first_ball = third_ball / 3
    second_ball = first_ball * 2
    result = second_ball
    return result

print(solution())