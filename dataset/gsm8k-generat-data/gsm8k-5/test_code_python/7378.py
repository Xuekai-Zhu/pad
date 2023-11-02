def solution():
    cones_tues = 12000  # 12,000 cones sold on Tuesday
    cones_wed = cones_tues * 2  # Cones sold on Wednesday are twice as many as those sold on Tuesday

    # Calculate total cones sold
    total_cones = cones_tues + cones_wed
    result = total_cones
    return result

print(solution())