def solution():
    total_mileage = 10  # Layla rode a total of 10 miles
    race_mileage = 4  # Layla rode 4 miles around the track at her faster, race pace
    slow_mileage = (total_mileage - race_mileage) / 2  # Layla rode the remaining miles slowly, both to and from the high school

    # Calculate the distance from Layla's house to the high school
    distance_to_high_school = slow_mileage
    result = distance_to_high_school
    return result

print(solution())