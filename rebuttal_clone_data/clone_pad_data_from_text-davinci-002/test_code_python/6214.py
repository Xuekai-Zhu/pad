def solution():
    plane1_passengers = 50
    plane2_passengers = 60
    plane3_passengers = 40
    plane1_speed = 600 - (2 * plane1_passengers)
    plane2_speed = 600 - (2 * plane2_passengers)
    plane3_speed = 600 - (2 * plane3_passengers)
    total_speed = plane1_speed + plane2_speed + plane3_speed
    total_passengers = plane1_passengers + plane2_passengers + plane3_passengers
    average_speed = total_speed / total_passengers
    result = average_speed
    return result

print(solution())