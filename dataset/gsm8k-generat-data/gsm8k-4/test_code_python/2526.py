def solution():
    """Nate went out to do his daily exercises. In 8 seconds, he ran a distance equal to four times the length of a football field. He rested for a while, then ran 500 more meters. If the field's length is 168 meters, how far did Nate ran?"""
    # Calculate the distance Nate ran in the first part
    football_field_length = 168
    distance_first_part = 4 * football_field_length

    # Add the distance Nate ran in the second part
    distance_second_part = 500

    # Calculate the total distance Nate ran
    total_distance = distance_first_part + distance_second_part

    result = total_distance
    return result

print(solution())