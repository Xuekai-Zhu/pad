def solution():
    tank_capacity = 8000
    initial_level = tank_capacity * 0.75
    water_used = initial_level * 0.40
    final_level = initial_level - water_used + (water_used * 0.30)
    result = final_level
    return result

print(solution())