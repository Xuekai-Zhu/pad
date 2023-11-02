def solution():
    """Nate went out to do his daily exercises. In 8 seconds, he ran a distance equal to four times the length of a football field. He rested for a while, then ran 500 more meters. If the field's length is 168 meters, how far did Nate ran?"""
    # Define the length of a football field in meters
    FIELD_LENGTH = 168

    # Calculate the distance Nate ran in the first part of his exercise
    distance1 = 4 * FIELD_LENGTH

    # Calculate the total distance Nate ran
    total_distance = distance1 + 500

    # Display the total distance Nate ran
    result = total_distance
    return result

print(solution())