def solution():
    num_quilts_1 = 7
    yards_1 = 21
    num_quilts_2 = 12

    # Use a proportion to find the required yards of material for 12 quilts
    yards_2 = (num_quilts_2 * yards_1) / num_quilts_1
    result = yards_2
    return result

print(solution())