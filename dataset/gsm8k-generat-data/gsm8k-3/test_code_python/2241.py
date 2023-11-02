def solution():
    """Darrel is an experienced tracker.  He can tell a lot about an animal by the footprints it leaves behind.  One day he saw a set of coyote footprints.  Based on the impressions, he could tell the animal was traveling east at 15 miles per hour, and that the animal left the prints 1 hour ago.  If the coyote continues to travel east at 15 miles per hour, and Darrell hops on his motorbike and travels east at 30 miles per hour, how long, in hours, will it take for Darrel to catch up to the coyote?"""
    # Define the speed of the coyote and Darrell on his motorbike
    COYOTE_SPEED = 15
    DARRELL_SPEED = 30

    # Define the time the coyote has been traveling
    coyote_time = 1

    # Calculate the distance the coyote has traveled
    coyote_distance = COYOTE_SPEED * coyote_time

    # Calculate the time it will take for Darrell to catch up to the coyote
    darrell_time = coyote_distance / (DARRELL_SPEED - COYOTE_SPEED)

    # Display the time it will take for Darrell to catch up to the coyote
    result = darrell_time
    return result

print(solution())