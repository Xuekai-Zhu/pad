def solution():
    """There were 140 kids in the junior prom. Of those, a fourth of them were dancers. Of the dancers, 25 danced the slow dance. How many of the dancer students did not slow dance?"""
    # Define the total number of students and the fraction of dancers
    total_students = 140
    dancers_fraction = 1/4

    # Calculate the number of dancers and the number of students who did not dance
    dancers = total_students * dancers_fraction
    non_dancers = total_students - dancers

    # Calculate the number of dancers who did not slow dance
    non_slow_dancers = dancers - 25

    # Return the result
    result = non_slow_dancers
    return result

print(solution())