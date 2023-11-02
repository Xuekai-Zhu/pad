def solution():
    full_battery = 60
    used_battery = 45
    exam_length = 2
    remaining_battery = full_battery - used_battery - exam_length
    result = remaining_battery
    return result

print(solution())