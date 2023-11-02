def solution():
    loads_of_laundry = 8
    minutes_per_load = 45
    minutes_per_hour = 60
    hours_per_load = (minutes_per_load / minutes_per_hour) + 1
    total_hours = loads_of_laundry * hours_per_load
    result = total_hours
    return result

print(solution())