def solution():
    """Nate went out to do his daily exercises. In 8 seconds, he ran a distance equal to four times the length of a football field. He rested for a while, then ran 500 more meters. If the field's length is 168 meters, how far did Nate ran?"""
    football_field_length = 168
    distance_covered_in_8_seconds = 4 * football_field_length
    additional_distance_covered = 500
    total_distance_covered = distance_covered_in_8_seconds + additional_distance_covered
    result = total_distance_covered
    return result

print(solution())