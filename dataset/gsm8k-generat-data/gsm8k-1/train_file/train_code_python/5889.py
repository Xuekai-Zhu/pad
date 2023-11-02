def solution():
    """Laura’s House is a 20-mile round trip from her school. The supermarket is 10 miles farther away from the school. If Laura drives to school every morning and two afternoons a week drives to the supermarket. How many miles does Laura driver per week?"""
    round_trip_to_school = 2 * 20
    round_trip_to_supermarket = 2 * (20 + 10)
    total_miles = round_trip_to_school * 5 + round_trip_to_supermarket * 2
    result = total_miles
    return result

print(solution())