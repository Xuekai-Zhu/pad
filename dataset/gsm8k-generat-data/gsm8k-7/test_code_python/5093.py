def solution():
    total_rides = 8 + 16  # Maurice's rides plus Matt's additional rides
    matt_rides = 3 * (total_rides - 8)  # Matt's rides are three times Maurice's before visit
    maurice_rides = matt_rides / 4  # Maurice's rides are 1/4 of Matt's
    result = maurice_rides
    return result

print(solution())