def solution():
    """Joe played catch with Derek and Tammy. He caught the ball 23 times. Derek made four less than double the catches Joe did. Tammy caught the ball sixteen more than a third of the times Derek did. How many times did Tammy catch the ball?"""
    joe_catches = 23
    derek_catches = 2 * joe_catches - 4
    tammy_catches = (1/3) * derek_catches + 16
    result = tammy_catches
    return result

print(solution())