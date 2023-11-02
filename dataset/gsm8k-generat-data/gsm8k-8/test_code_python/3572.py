def solution():
    # Calculate the number of blouses Eliza ironed
    blouses = 2 * 60 // 15  # 2 hours converted to minutes divided by 15 minutes per blouse
    # Calculate the number of dresses Eliza ironed
    dresses = 3 * 60 // 20  # 3 hours converted to minutes divided by 20 minutes per dress

    # Calculate the total number of clothes Eliza ironed
    total_clothes = blouses + dresses
    result = total_clothes
    return result

print(solution())