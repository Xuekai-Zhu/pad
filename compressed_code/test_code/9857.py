def solution():
    
    fabric_per_pants = 8.5
    num_pants = 7
    yards_of_fabric = 3.5
    feet_of_fabric = yards_of_fabric * 3
    total_fabric_needed = fabric_per_pants * num_pants
    remaining_fabric = total_fabric_needed - feet_of_fabric
    result = remaining_fabric
    return result

print(solution())