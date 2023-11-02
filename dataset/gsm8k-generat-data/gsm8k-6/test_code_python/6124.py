def solution():
    # Convert yards of fabric to feet
    yards_to_feet = 3  # 1 yard is equal to 3 feet
    fabric_needed = 5.5 * 4  # 4 dresses require 5.5 yards each of fabric
    total_fabric = fabric_needed * yards_to_feet  # Total fabric needed in feet
    remaining_fabric = total_fabric - (7 * 12)  # 7 feet of fabric given, converted to inches
    result = remaining_fabric / 12  # Convert remaining inches to feet
    return result

print(solution())