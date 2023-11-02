def solution():
    """Sara builds a birdhouse that is 1 foot wide, 2 feet tall and 2 feet deep. Jake builds a birdhouse that is 16 inches wide, 20 inches tall and 18 inches deep. What is the difference in volume between the two birdhouses?"""
    sara_volume = 1 * 2 * 2
    jake_volume = (16/12) * (20/12) * (18/12)  # convert inches to feet
    volume_difference = sara_volume - jake_volume
    result = volume_difference
    return result

print(solution())