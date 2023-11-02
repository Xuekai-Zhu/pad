def solution():
    """Jack cycles from his home to the store. Then he cycles, at the same speed, 50 miles to his friend Peter. It takes Jack twice as long to go from his home to the store as it takes to go from the store to his friend. If Peter and Jack now cycle back to the store together, how many miles in total have they cycled today?"""
    distance_to_store = None
    distance_to_friend = 50
    total_distance = None

    # Let's first find the distance from home to the store:
    # Assume that Jack's speed is S miles/hour.
    # Then the time taken to go from the store to the friend is 50/S hours.
    # Since it takes twice as long to go from home to store, the time taken to go from home to store is 100/S.
    # We can then use the formula Distance = Speed * Time to find the distance from home to store.
    # We know that Distance_home_to_store = 2 * Distance_store_to_friend
    # Combining these two equations we get:
    # 2 * Distance_store_to_friend = S * (100/S)
    # Distance_store_to_friend = 50
    # Therefore, S = 200/5 = 40 miles/hour
    speed = 40
    time_to_store = 100 / speed
    distance_to_store = time_to_store * speed

    # Now that we know the distances, we can find the total distance cycled.
    total_distance = distance_to_store + distance_to_friend + distance_to_store

    result = total_distance
    return result

print(solution())