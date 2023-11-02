def solution():
    amtrak_operates_trains = True
    amtrak_operates_buses = True
    bus_has_four_wheels = True
    if amtrak_operates_buses and bus_has_four_wheels:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())