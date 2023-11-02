def solution():
    
    batter_time = 20
    bake_time = 30
    cool_time = 2 * 60 + 10
    total_time = batter_time + bake_time + cool_time + frost_time
    daily_time = 5 * 60
    latest_time = daily_time - total_time
    result = latest_time
    return result

print(solution())