def solution():
    """There were 140 kids in the junior prom. Of those, a fourth of them were dancers. Of the dancers, 25 danced the slow dance. How many of the dancer students did not slow dance?"""
    total_students = 140
    dancers = total_students / 4
    slow_dancers = 25
    non_slow_dancers = dancers - slow_dancers
    result = non_slow_dancers
    return result

print(solution())