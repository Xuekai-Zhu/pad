def solution():
    """Jonsey is awake for 2/3 of the day and spends 1/2 her time awake playing outside and the rest inside. Her brother, Riley, is awake for 3/4 of the day and spends 1/3 of his day outside and the rest inside. How much time, on average, do they spend inside?"""
    # Define the fractions of time Jonsey and Riley spend awake
    JONSEY_AWAKE_FRACTION = 2/3
    RILEY_AWAKE_FRACTION = 3/4

    # Calculate the time Jonsey spends inside
    JONSEY_INSIDE_FRACTION = 1/2
    jonsey_inside_time = JONSEY_AWAKE_FRACTION * (1 - JONSEY_INSIDE_FRACTION)

    # Calculate the time Riley spends inside
    RILEY_INSIDE_FRACTION = 2/3
    riley_inside_time = RILEY_AWAKE_FRACTION * (1 - RILEY_INSIDE_FRACTION)

    # Calculate the average time they spend inside
    avg_inside_time = (jonsey_inside_time + riley_inside_time) / 2

    # Display the average time they spend inside
    result = avg_inside_time
    return result

print(solution())