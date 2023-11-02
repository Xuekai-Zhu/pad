def solution():
    maurice_rides = 8
    matt_rides = maurice_rides + 16
    total_matt_rides = matt_rides * 3
    maurice_previous_rides = total_matt_rides / 3 - 16
    result = maurice_previous_rides
    return result

print(solution())