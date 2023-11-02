def solution():
    """Alex is on a cross-country bike trip. After starting this morning, he manages an average speed over flat ground of about 20 miles per hour. Four and a half hours later, the road started to incline upwards enough that he could only manage 12 miles per hour. Two and a half hours later, though, the road declined downhill and was able to mostly coast at 24 miles per hour. Unfortunately, he only got to enjoy this for one and a half hours before he punctured a tire. He had forgotten to pack a repair kit, so he had to walk his bike the rest of the way to the next town. If the next town was 164 miles from where he started this morning, how far did Alex have to walk?"""
    # calculate distance covered while biking
    flat_speed = 20
    flat_time = 4.5
    flat_distance = flat_speed * flat_time

    uphill_speed = 12
    uphill_time = 2.5
    uphill_distance = uphill_speed * uphill_time

    downhill_speed = 24
    downhill_time = 1.5
    downhill_distance = downhill_speed * downhill_time

    total_distance_biked = flat_distance + uphill_distance + downhill_distance

    # calculate distance walked
    total_distance = 164
    distance_walked = total_distance - total_distance_biked

    result = distance_walked
    return result

print(solution())