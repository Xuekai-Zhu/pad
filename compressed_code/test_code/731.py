def solution():
    
    blue_shirts = 26
    brown_shirts = 36
    half_blue = blue_shirts / 2
    third_brown = brown_shirts / 3
    remaining_blue = blue_shirts - half_blue
    remaining_brown = brown_shirts - third_brown
    total_shirts = remaining_blue + remaining_brown
    result = total_shirts
    return result

print(solution())