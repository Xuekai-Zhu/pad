def solution():
    """Vins rides his bike 6 miles to school. He rides home a different route that is 7 miles long. 
    This week, Vins rode to school and back 5 times. How many miles did Vins ride his bike this week?"""
    miles_to_school = 6
    miles_from_school = 7
    total_miles_per_trip = miles_to_school + miles_from_school
    number_of_trips = 5
    total_miles = total_miles_per_trip * number_of_trips
    result = total_miles
    return result

print(solution())