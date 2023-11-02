def solution():
    # Calculate the total distance they need to row
    distance = ((80 - 50) / 2) * 10 # calculate the distance from 50 to 80 yards, assuming the width increases uniformly by 2 yards every 10 meters
    distance += 50 # add the initial 50 yards
    # Calculate the time it will take for them to cover the distance
    time = distance / 5 # given they row at 5 m/s
    result = time
    return result

print(solution())