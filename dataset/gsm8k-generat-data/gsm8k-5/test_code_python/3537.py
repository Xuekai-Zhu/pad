def solution():
    quilts_per_yard = 7/21  # Jennie can make 7 quilts with 21 yards of material
    quilts_needed = 12  # Jennie wants to make 12 quilts

    # Calculate the yards of material required to make 12 quilts
    yards_needed = quilts_needed / quilts_per_yard
    result = yards_needed
    return result

print(solution())