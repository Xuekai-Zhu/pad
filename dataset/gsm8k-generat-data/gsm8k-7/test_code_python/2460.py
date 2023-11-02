def solution():
    pay_per_mile = 0.4
    distance = 400
    round_trip_distance = distance * 2

    # Calculate the total pay for a round trip
    total_pay = round_trip_distance * pay_per_mile
    result = total_pay
    return result

print(solution())