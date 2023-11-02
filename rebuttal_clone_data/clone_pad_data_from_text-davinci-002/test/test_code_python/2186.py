def solution():
    leak_percent = 10
    total_liters = 220
    liters_lost = total_liters * (leak_percent / 100)
    liters_left = total_liters - liters_lost
    result = liters_left
    return result

print(solution())