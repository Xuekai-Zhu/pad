def solution():
    
    fabric_per_pant = 8.5
    total_pants = 7
    yards_of_fabric = 3.5
    feet_of_fabric = yards_of_fabric * 3
    total_feet_of_fabric_needed = fabric_per_pant * total_pants
    feet_of_fabric_needed = total_feet_of_fabric_needed - feet_of_fabric
    result = feet_of_fabric_needed
    return result

print(solution())