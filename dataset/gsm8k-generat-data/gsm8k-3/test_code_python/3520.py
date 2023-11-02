def solution():
    """Haley is getting ready to watch a comet fly over her house. She spends two hours shopping for a telescope, half an hour getting everything set up in the backyard, three times the setup time making snacks, and 20 minutes watching the comet. What percentage of the total time she spent on all those activities was spent watching the comet, rounded to the nearest percent?"""
    # Define the time spent on each activity in minutes
    telescope_shopping_time = 120
    setup_time = 30
    snack_making_time = setup_time * 3
    comet_watching_time = 20

    # Calculate the total time spent in minutes
    total_time = (telescope_shopping_time + setup_time + snack_making_time + comet_watching_time)

    # Calculate the percentage of time spent watching the comet
    comet_percent = round((comet_watching_time / total_time) * 100)

    # Display the percentage of time spent watching the comet
    result = f"{comet_percent}%"
    return result

print(solution())