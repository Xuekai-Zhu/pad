def solution():
    """Haley is getting ready to watch a comet fly over her house. She spends two hours shopping for a telescope, half an hour getting everything set up in the backyard, three times the setup time making snacks, and 20 minutes watching the comet. What percentage of the total time she spent on all those activities was spent watching the comet, rounded to the nearest percent?"""
    telescope_time = 2 * 60 # convert hours to minutes
    setup_time = 0.5 * 60 # convert half an hour to minutes
    snack_time = setup_time * 3
    comet_time = 20
    total_time = telescope_time + setup_time + snack_time + comet_time
    percent_time_watching_comet = (comet_time / total_time) * 100
    result = round(percent_time_watching_comet)
    return result

print(solution())