def solution():
    """Darrel is an experienced tracker. He can tell a lot about an animal by the footprints it leaves behind. One day he saw a set of coyote footprints. Based on the impressions, he could tell the animal was traveling east at 15 miles per hour, and that the animal left the prints 1 hour ago. If the coyote continues to travel east at 15 miles per hour, and Darrell hops on his motorbike and travels east at 30 miles per hour, how long, in hours, will it take for Darrel to catch up to the coyote?"""
    coyote_speed = 15
    darrel_speed = 30
    time_elapsed = 1
    distance_traveled_by_coyote = coyote_speed * time_elapsed
    distance_difference = distance_traveled_by_coyote
    time_to_catch_up = distance_difference / (darrel_speed - coyote_speed)
    result = time_to_catch_up
    return result

print(solution())