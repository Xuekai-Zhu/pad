def solution():
    jerome_speed = 4  # Jerome runs at 4 MPH
    jerome_time = 6  # Jerome takes 6 hours to run the trail
    nero_time = 3  # Nero takes 3 hours to run the trail

    # Calculate the distance of the trail
    distance = jerome_speed * jerome_time

    # Calculate Nero's speed
    nero_speed = distance / nero_time
    result = nero_speed
    return result

print(solution())