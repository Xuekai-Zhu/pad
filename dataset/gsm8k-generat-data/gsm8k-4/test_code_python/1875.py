def solution():
    """Tom's rabbit can run at 25 miles per hour. His cat can run 20 miles per hour. The cat gets a 15-minute head start. In hours, how long will it take for the rabbit to catch up?"""
    # Define the speed of the rabbit and the cat
    rabbit_speed = 25
    cat_speed = 20

    # Define the time the cat has a head start
    head_start_time = 0.25

    # Calculate how far the cat travels during the head start time
    cat_distance = cat_speed * head_start_time

    # Determine how long it takes for the rabbit to catch up to the cat
    catch_up_time = cat_distance / (rabbit_speed - cat_speed)

    # Return the result in hours, rounded to two decimal places
    result = round(catch_up_time, 2)
    return result

print(solution())