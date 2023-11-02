def solution():
    """Marsha works as a delivery driver for Amazon. She has to drive 10 miles to deliver her first package, 28 miles to deliver her second package, and half that long to deliver her third package. If she gets paid $104 for the day, how many dollars does she get paid per mile?"""
    total_distance = 10 + 28 + (28 / 2)
    pay_per_mile = 104 / total_distance
    result = pay_per_mile
    return result

print(solution())