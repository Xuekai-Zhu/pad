def solution():
    bus_speed = 60
    dog_speed = 45
    if dog_speed > bus_speed:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())