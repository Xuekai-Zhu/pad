def solution():
    """Tom's rabbit can run at 25 miles per hour.  His cat can run 20 miles per hour.  The cat gets a 15-minute head start.  In hours, how long will it take for the rabbit to catch up?"""
    # Define the speeds of the rabbit and the cat
    RABBIT_SPEED = 25
    CAT_SPEED = 20

    # Define the time the cat has as a head start
    cat_head_start = 0.25 # 15 minutes = 0.25 hours

    # Calculate the distance the cat has traveled during its head start
    cat_distance = cat_head_start * CAT_SPEED

    # Define the distance the rabbit needs to catch up to the cat
    distance_to_catch_up = cat_distance

    # Calculate the time it takes for the rabbit to catch up
    time_to_catch_up = distance_to_catch_up / (RABBIT_SPEED - CAT_SPEED)

    # Display the time it takes for the rabbit to catch up
    result = time_to_catch_up
    return result

print(solution())