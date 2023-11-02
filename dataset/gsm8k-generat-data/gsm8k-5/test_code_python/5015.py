def solution():
    # Let x be the time for Jack to cycle from the store to Peter's house
    # Then 2x is the time for Jack to cycle from his home to the store
    time_to_store = 2*x
    time_to_peter = x

    # Let s be Jack's speed
    # Then distance to store = s*time_to_store and distance to Peter = s*time_to_peter = 50
    distance_to_store = s*time_to_store
    distance_to_peter = 50

    # Total distance cycled by Jack = distance to store + distance to Peter + distance back to store with Peter
    total_distance = distance_to_store + distance_to_peter + 2*distance_to_peter

    # Simplifying the equations above, we get:
    s = 50/(x)
    distance_to_store = 2*50/s
    total_distance = 4*distance_to_store

    result = total_distance
    return result

print(solution())