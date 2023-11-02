def solution():
    # Calculate the total number of bones buried by Barkley
    total_bones = 10 * 5  # 10 bones at the beginning of each month for 5 months
    buried_bones = total_bones - 8  # 8 bones left at the end of the 5th month
    result = buried_bones
    return result

print(solution())