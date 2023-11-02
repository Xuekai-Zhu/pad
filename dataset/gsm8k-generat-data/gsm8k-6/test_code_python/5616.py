def solution():
    # Calculate the speed of the dragon relative to Xena
    relative_speed = 30 - 15  # the dragon flies 30 feet per second and Xena runs 15 feet per second

    # Calculate the distance Xena can run before the dragon catches up
    safe_distance = 600 - 120  # Xena has a 600 foot head start, but the dragon can burn her within 120 feet

    # Calculate the time Xena has to get to the cave
    time = safe_distance / relative_speed
    result = time
    return result

print(solution())