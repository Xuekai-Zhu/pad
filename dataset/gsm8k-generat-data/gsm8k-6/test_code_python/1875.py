def solution():
    cat_speed = 20  # cat's speed in miles per hour
    rabbit_speed = 25  # rabbit's speed in miles per hour

    # Convert 15 minutes head start of the cat to hours
    cat_head_start = 15 / 60

    # Calculate how far the cat runs during the head start
    cat_distance = cat_speed * cat_head_start

    # Calculate the time it takes for the rabbit to catch up with the cat
    catch_up_time = cat_distance / (rabbit_speed - cat_speed)

    result = catch_up_time
    return result

print(solution())