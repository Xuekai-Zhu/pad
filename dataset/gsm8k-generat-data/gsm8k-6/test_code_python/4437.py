def solution():
    # Calculate the total distance of the relay run this year
    total_distance = 300 * 4  # this year's race will be 4 times as long as last year's, which was 300 meters

    # Calculate the distance between each table
    distance_between_tables = total_distance / 6  

    # Calculate the distance between table 1 and table 3
    distance_1_to_3 = distance_between_tables * 2 

    result = distance_1_to_3
    return result

print(solution())