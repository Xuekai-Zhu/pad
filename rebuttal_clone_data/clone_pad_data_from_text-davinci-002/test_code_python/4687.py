def solution():
    bus_leave_time = 8
    bus_arrive_time = bus_leave_time - 0.5
    time_difference = bus_arrive_time - bus_leave_time
    result = abs(time_difference)
    return result

print(solution())