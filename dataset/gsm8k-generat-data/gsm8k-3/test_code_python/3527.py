def solution():
    """Marsha works as a delivery driver for Amazon. She has to drive 10 miles to deliver her first package, 28 miles to deliver her second package, and half that long to deliver her third package. If she gets paid $104 for the day, how many dollars does she get paid per mile?"""
    # Define the distances Marsha drives
    distance_1 = 10
    distance_2 = 28
    distance_3 = distance_2 / 2

    # Calculate the total distance Marsha drives
    total_distance = distance_1 + distance_2 + distance_3

    # Calculate Marsha's pay per mile
    pay_per_mile = 104 / total_distance

    # Display Marsha's pay per mile
    result = pay_per_mile
    return result

print(solution())