def solution():
    """Jo-Bob hopped into the hot air balloon, released the anchor rope, and pulled on the lift chain,
    which ignited the flame and provided the warm air that caused the balloon to rise. When the lift chain was
    pulled, the balloon would rise at a rate of 50 feet per minute. But when the chain was not being pulled,
    the balloon would slowly descend at a rate of 10 feet per minute. During his balloon ride,
    he pulled the chain for 15 minutes, then released the rope for 10 minutes, then pulled the chain for another
    15 minutes, and finally released the chain and allowed the balloon to slowly descend back to the earth.
    During his balloon ride, what was the highest elevation reached by the balloon?"""
    pull_time = 15
    release_time = 10
    ascend_rate = 50
    descend_rate = 10
    max_elevation = 0

    # calculate height during first pull
    current_elevation = ascend_rate * pull_time
    max_elevation = max(max_elevation, current_elevation)

    # calculate height during first release
    current_elevation -= descend_rate * release_time

    # calculate height during second pull
    current_elevation += ascend_rate * pull_time
    max_elevation = max(max_elevation, current_elevation)

    # calculate height during descent
    time_remaining = 60 - (2 * pull_time + release_time)
    current_elevation += (ascend_rate - descend_rate) * time_remaining
    max_elevation = max(max_elevation, current_elevation)

    result = max_elevation
    return result

print(solution())