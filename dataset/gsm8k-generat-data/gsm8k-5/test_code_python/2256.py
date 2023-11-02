def solution():
    total_time = 4 * 60  # Carson is spending 4 hours at the carnival, converted to minutes

    # Calculate the total time spent on roller coaster and tilt-a-whirl
    coaster_time = 4 * 30  # Carson rides the roller coaster 4 times, with a 30 minute wait each time
    tilt_time = 60  # Carson rides the tilt-a-whirl once, with a 60 minute wait

    remaining_time = total_time - coaster_time - tilt_time  # Calculate the remaining time for Carson to ride the giant slide

    # Calculate how many times Carson can ride the giant slide
    slide_time = 15  # Each ride on the giant slide takes 15 minutes, including wait time
    times_on_slide = remaining_time // slide_time

    result = times_on_slide
    return result

print(solution())