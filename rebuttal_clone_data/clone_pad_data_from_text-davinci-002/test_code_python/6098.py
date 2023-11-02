def solution():
    steps_matt = 20
    steps_tom = steps_matt + 5
    time_matt = 220 / steps_matt
    steps_tom_total = steps_tom * time_matt
    result = steps_tom_total
    return result

print(solution())