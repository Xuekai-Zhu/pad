def solution():
    ride_fee = 2  # Michelle pays a ride fee of $2 as soon as she enters the taxi
    distance = 4  # Michelle's ride is 4 miles in total
    charge_per_mile = 2.5  # The taxi charges $2.5 per mile

    # Calculate the total cost of the ride
    total_cost = ride_fee + (distance * charge_per_mile)

    result = total_cost
    return result

print(solution())