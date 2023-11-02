def solution():
    """At football tryouts, the coach wanted to see who could throw the ball the farthest. Parker threw the ball 16 yards. Grant threw the ball 25 percent farther than Parker and Kyle threw the ball 2 times farther than Grant. Compared to Parker, how much farther did Kyle throw the ball?"""
    # Define Parker's throw distance
    parker_distance = 16

    # Calculate Grant's throw distance
    grant_distance = parker_distance * 1.25

    # Calculate Kyle's throw distance
    kyle_distance = grant_distance * 2

    # Calculate the difference between Kyle's throw distance and Parker's throw distance
    difference = kyle_distance - parker_distance

    # return the result
    result = difference
    return result

print(solution())