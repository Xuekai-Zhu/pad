def solution():
    """The sum of the ages of two friends, Alma and Melina, is twice the total number of points Alma scored in a test. If Melina is three times as old as Alma, and she is 60, calculate Alma's score in the test?"""
    melina_age = 60
    alma_age = melina_age / 3
    alma_score = (alma_age + melina_age) / 2
    result = alma_score
    return result

print(solution())