def solution():
    
    total_clothes = 18 + 12 + 17 + 13
    cycles_needed = total_clothes // 15
    if total_clothes % 15 != 0:
        cycles_needed += 1
    washing_time = cycles_needed * 45
    washing_time_in_hours = washing_time / 60
    result = washing_time_in_hours
    return result

print(solution())