def solution():
    """Jack cycles from his home to the store. Then he cycles, at the same speed, 50 miles to his friend Peter. It takes Jack twice as long to go from his home to the store as it takes to go from the store to his friend. If Peter and Jack now cycle back to the store together, how many miles in total have they cycled today?"""
    distance_peter = 50
    time_store_to_peter = 1
    time_home_to_store = 2
    total_distance = (distance_peter * 2) + distance_peter
    result = total_distance
    return result

print(solution())