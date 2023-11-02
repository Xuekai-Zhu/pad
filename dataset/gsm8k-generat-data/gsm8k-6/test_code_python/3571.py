def solution():
    # Calculate the total distance Vins rides in one round trip
    round_trip_distance = 6 + 7

    # Calculate the total distance Vins rides in one day
    daily_distance = round_trip_distance * 2

    # Calculate the total distance Vins rides in one week
    weekly_distance = daily_distance * 5

    result = weekly_distance
    return result

print(solution())