def solution():
    """Marsha works as a delivery driver for Amazon. She has to drive 10 miles to deliver her first package, 28 miles to deliver her second package, and half that long to deliver her third package. If she gets paid $104 for the day, how many dollars does she get paid per mile?"""
    distance_first_package = 10
    distance_second_package = 28
    distance_third_package = distance_second_package / 2
    total_distance = distance_first_package + distance_second_package + distance_third_package
    payment = 104
    payment_per_mile = payment / total_distance
    result = payment_per_mile
    return result

print(solution())