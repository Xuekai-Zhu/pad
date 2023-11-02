def solution():
    # Define the ride distance and fees
    ride_distance = 4
    ride_fee_per_mile = 2.5
    ride_fee_fixed = 2

    # Calculate the total ride fee
    total_ride_fee = ride_fee_fixed + ride_distance * ride_fee_per_mile
    result = total_ride_fee
    return result

print(solution())