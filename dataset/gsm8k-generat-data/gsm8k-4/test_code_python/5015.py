def solution():
    """Jack cycles from his home to the store. Then he cycles, at the same speed, 50 miles to his friend Peter. It takes Jack twice as long to go from his home to the store as it takes to go from the store to his friend. If Peter and Jack now cycle back to the store together, how many miles in total have they cycled today?"""
    # Calculate the time it takes to go from the store to Peter's house
    store_to_peter_time = x

    # Calculate the time it takes to go from Jack's house to the store
    jack_to_store_time = 2 * store_to_peter_time

    # Calculate the distance from Jack's house to the store
    jack_to_store_distance = y

    # Calculate the total distance cycled by Jack
    jack_distance = jack_to_store_distance + 50

    # Calculate the distance cycled by both Peter and Jack
    total_distance = jack_to_store_distance + 2 * (50 - jack_to_store_distance)

    # return the result
    result = total_distance
    return result

print(solution())