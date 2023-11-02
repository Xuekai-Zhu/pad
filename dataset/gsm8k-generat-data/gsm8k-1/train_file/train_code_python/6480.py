def solution():
    """Sara builds a birdhouse that is 1 foot wide, 2 feet tall and 2 feet deep. Jake builds a birdhouse that is 16 inches wide, 20 inches tall and 18 inches deep. What is the difference in volume between the two birdhouses?"""
    sara_width = 1
    sara_height = 2
    sara_depth = 2
    jake_width = 16 / 12  # converting inches to feet
    jake_height = 20 / 12
    jake_depth = 18 / 12
    sara_volume = sara_width * sara_height * sara_depth
    jake_volume = jake_width * jake_height * jake_depth
    volume_difference = sara_volume - jake_volume
    result = volume_difference
    return result

print(solution())