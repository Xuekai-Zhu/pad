def solution():
    tank1_capacity = 300
    tank1_filled = 300
    tank2_capacity = 450
    tank2_filled = 202.5
    remaining_liters = tank2_capacity - tank2_filled
    result = tank1_filled + remaining_liters
    return result

print(solution())