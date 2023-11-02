def solution():
    telescope_shopping_time = 2  # hours
    setup_time = 0.5  # hours
    snack_making_time = setup_time * 3  # hours
    comet_watching_time = 20  # minutes

    # Convert all times to minutes and calculate total time in minutes
    total_time = (telescope_shopping_time + setup_time + snack_making_time + comet_watching_time/60) * 60

    # Calculate percentage of time spent watching the comet and round to nearest percent
    comet_percentage = round((comet_watching_time / total_time) * 100)

    result = comet_percentage
    return result

print(solution())