def solution():
    """
    At football tryouts, the coach wanted to see who could throw the ball the farthest. Parker threw the ball 16 yards.
    Grant threw the ball 25 percent farther than Parker and Kyle threw the ball 2 times farther than Grant.
    Compared to Parker, how much farther did Kyle throw the ball?
    """
    parker_distance = 16
    grant_distance = parker_distance + (parker_distance * 0.25)
    kyle_distance = grant_distance * 2
    difference = kyle_distance - parker_distance
    result = difference
    return result

print(solution())