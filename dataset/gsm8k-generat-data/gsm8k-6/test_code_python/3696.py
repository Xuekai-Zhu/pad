def solution():
    distance_to_school = 7  # kilometers to school
    extra_distance_on_friday = 2  # extra 2 kilometers on Friday
    total_distance_per_day = distance_to_school * 2  # total distance covered per day
    distance_covered_from_Monday_to_Thursday = total_distance_per_day * 4  # distance covered from Monday to Thursday
    distance_covered_on_Friday = (total_distance_per_day + extra_distance_on_friday)  # distance covered on Friday
    total_distance_covered = distance_covered_from_Monday_to_Thursday + distance_covered_on_Friday  # total distance covered for the week
    
    result = total_distance_covered
    return result

print(solution())