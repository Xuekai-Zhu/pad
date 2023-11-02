def solution():
    number_of_upstairs = 3
    number_of_downstairs = 6
    steps_per_flight = 12
    inches_per_step = 8
    feet_per_flight = steps_per_flight * inches_per_step / 12
    feet_traveled = (number_of_upstairs - number_of_downstairs) * feet_per_flight
    result = feet_traveled
    return result

print(solution())