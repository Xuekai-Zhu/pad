def solution():
    # Define the speeds of the rabbit and cat
    rabbit_speed = 25
    cat_speed = 20

    # Convert the cat's head start of 15 minutes to hours
    cat_head_start = 0.25

    # Calculate the distance between the rabbit and cat at the start
    start_distance = cat_head_start * cat_speed

    # Calculate the time it takes for the rabbit to catch up to the cat
    time_to_catch_up = start_distance / (rabbit_speed - cat_speed)

    result = time_to_catch_up
    return result

print(solution())