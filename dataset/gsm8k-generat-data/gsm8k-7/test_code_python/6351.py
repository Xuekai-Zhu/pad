def solution():
    telegraph_road_length = 162  # kilometers
    pardee_road_length = 12000  # meters

    # Convert Pardee Road length to kilometers
    pardee_road_length_km = pardee_road_length / 1000

    # Calculate the difference in length between Telegraph Road and Pardee Road
    difference = telegraph_road_length - pardee_road_length_km
    result = difference
    return result

print(solution())