def solution():
    monday_distance_km = 9
    wednesday_distance_m = 4816
    friday_distance_m = 2095

    # Convert Monday's distance to meters
    monday_distance_m = monday_distance_km * 1000

    # Calculate the total distance Hannah ran on Wednesday and Friday
    wed_fri_distance_m = wednesday_distance_m + friday_distance_m

    # Calculate the difference between Monday's distance and the total distance on Wednesday and Friday
    difference_m = monday_distance_m - wed_fri_distance_m
    result = difference_m
    return result

print(solution())