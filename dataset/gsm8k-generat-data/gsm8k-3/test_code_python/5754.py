def solution():
    """Alex is on a cross-country bike trip. After starting this morning, he manages an average speed over flat ground of about 20 miles per hour. Four and a half hours later, the road started to incline upwards enough that he could only manage 12 miles per hour. Two and a half hours later, though, the road declined downhill and was able to mostly coast at 24 miles per hour. Unfortunately, he only got to enjoy this for one and a half hours before he punctured a tire. He had forgotten to pack a repair kit, so he had to walk his bike the rest of the way to the next town. If the next town was 164 miles from where he started this morning, how far did Alex have to walk?"""
    # Calculate the distance traveled on flat ground
    distance_flat = 20 * 4.5

    # Calculate the distance traveled uphill
    distance_uphill = 12 * 2.5

    # Calculate the distance traveled downhill
    distance_downhill = 24 * 1.5

    # Calculate the total distance traveled
    total_distance = distance_flat + distance_uphill + distance_downhill

    # Calculate the distance Alex had to walk
    distance_walked = 164 - total_distance

    # Display the distance Alex had to walk
    result = distance_walked
    return result

print(solution())