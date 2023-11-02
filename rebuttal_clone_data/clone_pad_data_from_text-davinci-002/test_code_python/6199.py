def solution():
     building_A_floors = 4
     building_B_floors = 4 + 9
     building_C_floors = building_B_floors - 6 - (5 * building_B_floors)
     result = building_C_floors
     return result

print(solution())