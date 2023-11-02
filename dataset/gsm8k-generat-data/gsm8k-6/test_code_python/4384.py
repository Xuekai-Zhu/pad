def solution():
    current_speed = 500  # km/hr
    current_passengers = 200
    new_passengers = 400
    while current_passengers < new_passengers:
        current_speed /= 2
        current_passengers += 100
    result = current_speed
    return result

print(solution())