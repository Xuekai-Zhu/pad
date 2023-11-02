def solution():
    miles_to_school = 6
    miles_from_school = 7
    num_trips = 5

    # Calculate the total distance Vins rode to school and back
    total_distance = (miles_to_school + miles_from_school) * 2

    # Calculate the total distance Vins rode this week
    total_distance_week = total_distance * num_trips
    result = total_distance_week
    return result

print(solution())