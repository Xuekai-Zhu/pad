def solution():
    """There were 140 kids in the junior prom. Of those, a fourth of them were dancers. Of the dancers, 25 danced the slow dance. How many of the dancer students did not slow dance?"""
    total_students = 140
    dancer_students = total_students / 4
    slow_dance_students = 25
    non_slow_dance_students = dancer_students - slow_dance_students
    result = non_slow_dance_students
    return result

print(solution())