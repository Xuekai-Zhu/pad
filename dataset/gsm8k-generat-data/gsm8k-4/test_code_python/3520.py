def solution():
    """Haley is getting ready to watch a comet fly over her house. She spends two hours shopping for a telescope, half an hour getting everything set up in the backyard, three times the setup time making snacks, and 20 minutes watching the comet. What percentage of the total time she spent on all those activities was spent watching the comet, rounded to the nearest percent?"""
    # Define the time spent on each activity in minutes
    shopping_time = 2 * 60
    setup_time = 0.5 * 60
    snack_time = 3 * setup_time
    watching_time = 20

    # Calculate the total time spent in minutes
    total_time = shopping_time + setup_time + snack_time + watching_time

    # Calculate the percentage of time spent watching the comet
    watching_percentage = (watching_time / total_time) * 100

    # Round the percentage to the nearest integer
    result = round(watching_percentage)

    return result

print(solution())