def solution():
    """Jennie makes quilts. She can make 7 quilts with 21 yards of material. How many yards of material would be required to make 12 quilts?"""
    quilts_per_yard = 7
    yards_for_quilts = 21
    quilts_needed = 12
    yards_needed = (quilts_needed / quilts_per_yard) * yards_for_quilts
    result = yards_needed
    return result

print(solution())