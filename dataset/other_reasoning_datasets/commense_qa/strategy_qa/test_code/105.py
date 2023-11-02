def solution():
    earliest_motor_vehicles = 1890
    oscar_wilde_death_year = 1900
    if oscar_wilde_death_year > earliest_motor_vehicles:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())