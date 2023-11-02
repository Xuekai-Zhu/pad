def solution():
    jane_towels = 3
    kyla_towels = 5
    anthony_towels = 7
    jane_time = 5
    kyla_time = 10
    anthony_time = 20
    jane_rate = jane_towels / jane_time
    kyla_rate = kyla_towels / kyla_time
    anthony_rate = anthony_towels / anthony_time
    total_rate = jane_rate + kyla_rate + anthony_rate
    towels_per_hour = total_rate
    result = towels_per_hour
    return result

print(solution())