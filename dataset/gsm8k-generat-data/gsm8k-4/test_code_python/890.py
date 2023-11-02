def solution():
    """Javier is an Olympic javelin thrower. In the last Olympics, he threw the javelin three times. The first throw, he threw the javelin twice as far as he threw the javelin on his second throw, but only half as far as he threw it the third throw. If the sum of all three throws was 1050 meters, then how far, in meters, did he throw the javelin on his first throw?"""
    # Assign variables to the distances of the three throws
    throw1 = None
    throw2 = None
    throw3 = None

    # Use the given information to solve for the distances of the three throws
    # Let x be the distance of the second throw
    x = throw2

    # The first throw was twice as far as the second throw
    throw1 = 2 * x

    # The third throw was twice as far as the first throw
    throw3 = 2 * throw1

    # The sum of all three throws is 1050 meters
    total_distance = 1050

    # Substitute the values of throw1 and throw3 into the equation for total distance
    x + throw1 + throw3 = total_distance

    # Simplify the equation and solve for x
    x + 2x + 4x = total_distance
    7x = total_distance
    x = total_distance / 7

    # Substitute x back into the equations for throw1 and throw3 to find their values
    throw1 = 2 * x
    throw3 = 2 * throw1

    # The value of throw1 is the answer
    result = throw1
    return result

print(solution())