def solution():
    
    tank_1_gallons = 8
    tank_2_gallons = 8
    tank_3_gallons = tank_1_gallons - 2
    tank_4_gallons = tank_2_gallons - 2
    total_gallons = (tank_1_gallons + tank_2_gallons + tank_3_gallons + tank_4_gallons) * 4
    result = total_gallons
    return result

print(solution())