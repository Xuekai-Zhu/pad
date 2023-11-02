def solution():
    flights_of_stairs = 9
    feet_per_flight = 10
    inches_per_foot = 12
    inches_per_step = 18
    total_steps = flights_of_stairs * feet_per_flight * inches_per_foot / inches_per_step
    result = total_steps
    return result

print(solution())