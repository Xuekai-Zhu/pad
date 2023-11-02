def solution():
    round_trip_distance = 20  # Laura's house is a 20-mile round trip from her school
    supermarket_distance = 10  # The supermarket is 10 miles farther away from the school
    driving_frequency = 2  # Laura drives to the supermarket two afternoons a week
    total_miles = round_trip_distance * 5 + (supermarket_distance * driving_frequency)  # Laura drives to school every morning and to the supermarket twice a week

    result = total_miles
    return result

print(solution())