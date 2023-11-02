def solution():
    
    distance_one_way = 400
    distance_round_trip = distance_one_way * 2
    payment_per_mile = 0.40
    total_payment = distance_round_trip * payment_per_mile
    result = total_payment
    return result

print(solution())