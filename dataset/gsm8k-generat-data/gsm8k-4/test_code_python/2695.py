def solution():
    """Marcus spends 20 minutes giving his dog a bath and half as long blow-drying her. Then he takes her for a walk along a 3-mile trail. If Marcus walks at 6 miles per hour, how much time does he spend with his dog total?"""
    # Define the time spent giving the dog a bath
    bath_time = 20

    # Define the time spent blow-drying the dog
    drying_time = bath_time / 2

    # Define the distance of the walk in miles
    distance = 3

    # Calculate the time spent walking
    walk_time = distance / 6 * 60  # converting miles to minutes

    # Calculate the total time spent with the dog
    total_time = bath_time + drying_time + walk_time

    result = total_time
    return result

print(solution())