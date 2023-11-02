def solution():
    # Define Jace's driving speed and total driving time
    speed = 60
    total_time = 4 + 9.5 # accounting for 30-minute break

    # Calculate the distance Jace travels in each leg of the trip
    distance1 = speed * 4
    distance2 = speed * 9

    # Calculate the total distance Jace travels
    total_distance = distance1 + distance2

    # Calculate the final result
    result = total_distance
    return result

print(solution())