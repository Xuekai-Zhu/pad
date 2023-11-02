def solution():
    bath_time = 20  # Marcus spends 20 minutes giving his dog a bath
    dry_time = bath_time / 2  # Marcus spends half as long blow-drying the dog
    walk_distance = 3  # Marcus walks his dog along a 3-mile trail
    walk_speed = 6  # Marcus walks at a speed of 6 miles per hour

    # Calculate the time Marcus spends walking his dog
    walk_time = walk_distance / walk_speed

    # Calculate the total time Marcus spends with his dog
    total_time = (bath_time + dry_time + (walk_time * 60)) / 60
    result = total_time
    return result

print(solution())