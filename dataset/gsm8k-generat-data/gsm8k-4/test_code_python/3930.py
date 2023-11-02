def solution():
    """Jonsey is awake for 2/3 of the day and spends 1/2 her time awake playing outside and the rest inside. Her brother, Riley, is awake for 3/4 of the day and spends 1/3 of his day outside and the rest inside. How much time, on average, do they spend inside?"""
    # Define the fraction of time Jonsey is awake and the fraction of time she spends playing outside
    jonsey_awake_fraction = 2/3
    jonsey_outside_fraction = 1/2

    # Calculate the fraction of time Jonsey spends inside
    jonsey_inside_fraction = 1 - jonsey_outside_fraction

    # Define the fraction of time Riley is awake and the fraction of time he spends playing outside
    riley_awake_fraction = 3/4
    riley_outside_fraction = 1/3

    # Calculate the fraction of time Riley spends inside
    riley_inside_fraction = 1 - riley_outside_fraction

    # Calculate the average fraction of time they both spend inside
    average_inside_fraction = (jonsey_awake_fraction * jonsey_inside_fraction + riley_awake_fraction * riley_inside_fraction) / 2

    # Calculate the total time in hours they spend inside, based on an assumed 24-hour day
    total_inside_time = average_inside_fraction * 24

    # return the result
    result = total_inside_time
    return result

print(solution())