def solution():
    """Jamir and his two friends Sarah and Julien, go to their school's swimming pool to swim. Jamir swims 20 more meters per day than Sarah, who swims twice the distance Julien swims. They go to the swimming pool the whole week, swimming the same distances as before. If Julien swam 50 meters, what's the combined distance for three of them for the whole week?"""
    julien_distance = 50
    sarah_distance = julien_distance * 2
    jamir_distance = sarah_distance + 20
    total_distance = (julien_distance + sarah_distance + jamir_distance) * 7
    result = total_distance
    return result

print(solution())