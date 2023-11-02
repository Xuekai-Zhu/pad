def solution():
    """Vins rides his bike 6 miles to school. He rides home a different route that is 7 miles long. This week, Vins rode to school and back 5 times. How many miles did Vins ride his bike this week?"""
    # Define the distance to school and the distance home
    SCHOOL_DISTANCE = 6
    HOME_DISTANCE = 7

    # Calculate the total distance traveled in a round trip
    round_trip_distance = SCHOOL_DISTANCE + HOME_DISTANCE

    # Calculate the total distance traveled in 5 round trips
    total_distance = round_trip_distance * 5

    # return the result
    result = total_distance
    return result

print(solution())