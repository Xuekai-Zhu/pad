def solution():
    """Alex is on a cross-country bike trip. After starting this morning, he manages an average speed over flat ground of about 20 miles per hour. Four and a half hours later, the road started to incline upwards enough that he could only manage 12 miles per hour. Two and a half hours later, though, the road declined downhill and was able to mostly coast at 24 miles per hour. Unfortunately, he only got to enjoy this for one and a half hours before he punctured a tire. He had forgotten to pack a repair kit, so he had to walk his bike the rest of the way to the next town. If the next town was 164 miles from where he started this morning, how far did Alex have to walk?"""
    # Calculate the distance traveled at the first speed
    distance_1 = 20 * 4.5

    # Calculate the distance traveled at the second speed
    distance_2 = 12 * 2.5

    # Calculate the distance traveled at the third speed
    distance_3 = 24 * 1.5

    # Calculate the total distance traveled
    total_distance = distance_1 + distance_2 + distance_3

    # Calculate the distance left to travel on foot
    distance_left = 164 - total_distance

    # return the result
    result = distance_left
    return result

print(solution())