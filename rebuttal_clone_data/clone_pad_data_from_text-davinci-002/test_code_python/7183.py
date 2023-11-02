def solution():
    train_speed = 5
    coal_consumption = 2
    coal_remaining = 160
    distance = coal_remaining / coal_consumption * train_speed
    result = distance
    return result

print(solution())