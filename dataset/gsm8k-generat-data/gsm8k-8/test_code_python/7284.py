def solution():
    # Calculate the distance Talia drives from her house to the park and then to the grocery store
    park_distance = 5
    store_distance = 8
    total_distance = park_distance + store_distance

    # Calculate the distance Talia drives from the grocery store back to her house
    round_trip_distance = store_distance * 2

    # Calculate the total miles Talia drives that day
    total_miles = total_distance + round_trip_distance
    result = total_miles
    return result

print(solution())