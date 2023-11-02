def solution():
    """One pair of pants requires 8.5 feet of fabric. Nguyen needs to make 7 pairs of pants for the wedding. He has 3.5 yards of fabric. How many feet of fabric does Nguyen still need for the pants?"""
    fabric_per_pants = 8.5
    num_pants = 7
    yards_of_fabric = 3.5
    feet_of_fabric = yards_of_fabric * 3
    total_fabric_needed = fabric_per_pants * num_pants
    remaining_fabric = total_fabric_needed - feet_of_fabric
    result = remaining_fabric
    return result

print(solution())