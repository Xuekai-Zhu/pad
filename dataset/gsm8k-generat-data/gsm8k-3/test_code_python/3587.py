def solution():
    """There were 140 kids in the junior prom. Of those, a fourth of them were dancers. Of the dancers, 25 danced the slow dance. How many of the dancer students did not slow dance?"""
    # Calculate the number of dancers
    num_dancers = 140 // 4

    # Calculate the number of dancers who did not slow dance
    num_non_slow_dancers = num_dancers - 25

    # Display the result
    result = num_non_slow_dancers
    return result

print(solution())