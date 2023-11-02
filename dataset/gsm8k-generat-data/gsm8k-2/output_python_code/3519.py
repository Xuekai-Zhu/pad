def solution():
    """Haley is getting ready to watch a comet fly over her house. She spends two hours shopping for a telescope, half an hour getting everything set up in the backyard, three times the setup time making snacks, and 20 minutes watching the comet. What percentage of the total time she spent on all those activities was spent watching the comet, rounded to the nearest percent?"""
    telescope_setup_time = 2
    backyard_setup_time = 0.5
    snack_setup_time = 3 * backyard_setup_time
    comet_watching_time = 20/60 # Convert 20 minutes to hours
    total_time = telescope_setup_time + backyard_setup_time + snack_setup_time + comet_watching_time
    comet_percentage = (comet_watching_time/total_time) * 100
    result = round(comet_percentage)
    return result

print(solution())