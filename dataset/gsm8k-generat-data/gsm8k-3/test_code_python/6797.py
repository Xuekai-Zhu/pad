def solution():
    """Barney can perform 45 sit-ups in one minute. Carrie can do twice as many sit-ups per minute as Barney can. And Jerrie can do 5 more sit-ups per minute than Carrie can do. If Barney does sit-ups for 1 minute, and Carrie does sit-ups for two minutes, and Jerrie does sit-ups for three minutes, what would be the combined total number of sit-ups performed?"""
    # Define the sit-up rate for each individual
    barney_rate = 45
    carrie_rate = 2 * barney_rate
    jerrie_rate = carrie_rate + 5

    # Calculate the number of sit-ups each person can do
    barney_situps = barney_rate * 1
    carrie_situps = carrie_rate * 2
    jerrie_situps = jerrie_rate * 3

    # Calculate the total number of sit-ups performed
    total_situps = barney_situps + carrie_situps + jerrie_situps

    # Display the total number of sit-ups
    result = total_situps
    return result

print(solution())