def solution():
    """Javier is an Olympic javelin thrower.  In the last Olympics, he threw the javelin three times.  The first throw, he threw the javelin twice as far as he threw the javelin on his second throw, but only half as far as he threw it the third throw.  If the sum of all three throws was 1050 meters, then how far, in meters, did he throw the javelin on his first throw?"""
    # Let x be the distance of the second throw
    # Then the distance of the first throw is 2x
    # And the distance of the third throw is 4x
    x = 0 # initialize x

    # Solve for x
    for i in range(51): # loop through possible values of x
        total_distance = 2 * i + i + 4 * i # calculate the total distance
        if total_distance == 1050: # check if the total distance is 1050 meters
            x = i # if it is, set x to i and break out of the loop, since we have found our solution
            break

    # Calculate the distance of the first throw
    distance_1 = 2 * x

    # Display the distance of the first throw
    result = distance_1
    return result

print(solution())