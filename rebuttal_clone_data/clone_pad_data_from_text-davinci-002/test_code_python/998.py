def solution():
    full_pool = 60
    hose_gallons_per_minute = 1.6
    leak_gallons_per_minute = 0.1
    minutes_to_fill_pool = full_pool / (hose_gallons_per_minute - leak_gallons_per_minute)
    result = minutes_to_fill_pool
    return result

print(solution())