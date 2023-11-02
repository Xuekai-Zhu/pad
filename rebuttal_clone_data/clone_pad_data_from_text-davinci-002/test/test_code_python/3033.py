def solution():
     checkered_fabric_cost = 75
     plain_fabric_cost = 45
     cost_per_yard = 7.50
     number_of_yards_checkered = checkered_fabric_cost / cost_per_yard
     number_of_yards_plain = plain_fabric_cost / cost_per_yard
     total_yards = number_of_yards_checkered + number_of_yards_plain
     result = total_yards
     return result

print(solution())