def solution():
    """Marsha works as a delivery driver for Amazon. She has to drive 10 miles to deliver her first package, 28 miles to deliver her second package, and half that long to deliver her third package. If she gets paid $104 for the day, how many dollars does she get paid per mile?"""
    # Define the distances Marsha has to drive
    distance1 = 10
    distance2 = 28
    distance3 = distance2 / 2

    # Calculate the total distance driven
    total_distance = distance1 + distance2 + distance3

    # Calculate the pay per mile
    pay_per_mile = 104 / total_distance

    result = pay_per_mile
    return result

print(solution())