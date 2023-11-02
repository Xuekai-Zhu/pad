def solution():
    miles_traveled = 1000
    miles_per_hour_abel = 50
    miles_per_hour_alice = 40
    hours_traveled = miles_traveled / miles_per_hour_abel
    abel_arrival_time = hours_traveled * 60
    alice_arrival_time = miles_traveled / miles_per_hour_alice * 60
    time_difference = abel_arrival_time - alice_arrival_time
    result = time_difference
    return result

print(solution())