def solution():
    """Barney can perform 45 sit-ups in one minute. Carrie can do twice as many sit-ups per minute as Barney can.
    And Jerrie can do 5 more sit-ups per minute than Carrie can do.
    If Barney does sit-ups for 1 minute, and Carrie does sit-ups for two minutes,
    and Jerrie does sit-ups for three minutes, what would be the combined total number of sit-ups performed?"""
    # Define the number of sit-ups each person can do per minute
    barney_situps_per_minute = 45
    carrie_situps_per_minute = 2 * barney_situps_per_minute
    jerrie_situps_per_minute = carrie_situps_per_minute + 5

    # Calculate the total number of sit-ups each person can do for their given time
    barney_total_situps = barney_situps_per_minute * 1
    carrie_total_situps = carrie_situps_per_minute * 2
    jerrie_total_situps = jerrie_situps_per_minute * 3

    # Calculate the combined total number of sit-ups performed
    combined_total_situps = barney_total_situps + carrie_total_situps + jerrie_total_situps
    result = combined_total_situps
    return result

print(solution())