def solution():
    
    total_miles = 135 + 259 + 159 + 189
    charge_count = total_miles // 106
    if total_miles % 106 != 0:
        charge_count += 1

    result = charge_count
    return result

print(solution())