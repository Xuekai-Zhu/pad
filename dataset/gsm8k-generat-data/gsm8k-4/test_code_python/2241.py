def solution():
    """Darrel is an experienced tracker. He can tell a lot about an animal by the footprints it leaves behind. One day he saw a set of coyote footprints. Based on the impressions, he could tell the animal was traveling east at 15 miles per hour, and that the animal left the prints 1 hour ago. If the coyote continues to travel east at 15 miles per hour, and Darrell hops on his motorbike and travels east at 30 miles per hour, how long, in hours, will it take for Darrel to catch up to the coyote?"""
    # Calculate the distance the coyote has traveled
    coyote_distance = 15 * 1

    # Calculate the distance between Darrell and the coyote when Darrell starts tracking
    distance_between = coyote_distance

    # Calculate the relative speed between Darrell and the coyote
    relative_speed = 30 - 15

    # Calculate the time it will take for Darrell to catch up to the coyote
    time = distance_between / relative_speed

    # Return the result
    result = time
    return result

print(solution())