def solution():
    # Frank takes 5 steps back
    distance = -5
    # Frank then takes 10 steps forward
    distance += 10
    # Frank then takes 2 steps back
    distance -= 2
    # Frank then takes double the previous amount of steps, which is 2*10 = 20
    distance += 20

    result = distance
    return result

print(solution())