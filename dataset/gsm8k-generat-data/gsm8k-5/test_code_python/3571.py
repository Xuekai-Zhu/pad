def solution():
    distance_to_school = 6  # Vins rides 6 miles to school
    distance_from_school = 7  # Vins rides 7 miles from school back home
    round_trip_distance = distance_to_school + distance_from_school  # Total distance for a round trip
    number_of_round_trips = 5  # Vins made 5 round trips this week

    # Calculate the total distance Vins rode his bike this week
    total_distance = round_trip_distance * number_of_round_trips
    result = total_distance
    return result

print(solution())