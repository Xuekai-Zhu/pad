def solution():
    """Nate went out to do his daily exercises. In 8 seconds, he ran a distance equal to four times the length of a football field. He rested for a while, then ran 500 more meters. If the field's length is 168 meters, how far did Nate run?"""
    football_field = 168
    distance_first_run = 4 * football_field
    distance_second_run = 500
    total_distance = distance_first_run + distance_second_run
    result = total_distance
    return result

print(solution())