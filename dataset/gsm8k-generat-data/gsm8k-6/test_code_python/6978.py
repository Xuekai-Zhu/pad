def solution():
    # Calculate the total amount of meat needed by the pack
    total_meat_needed = (4 + 16) * 8 * 5  # 4 hunting wolves plus 16 pack wolves, each needing 8 pounds of meat per day, for 5 days

    # Calculate the number of deer each wolf needs to kill
    deer_needed = total_meat_needed / 200  # each deer contains 200 pounds of meat
    deer_per_wolf = deer_needed / 4  # divide by the number of hunting wolves
    
    result = deer_per_wolf
    return result

print(solution())