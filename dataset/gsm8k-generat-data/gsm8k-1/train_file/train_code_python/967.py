def solution():
    """Mary has 26 blue shirts and 36 brown shirts. If she gives away half of her blue shirts and a third of her brown shirts, how many shirts does she have left?"""
    blue_shirts = 26
    brown_shirts = 36
    half_blue = blue_shirts / 2
    third_brown = brown_shirts / 3
    total_given = half_blue + third_brown
    remaining_blue = blue_shirts - half_blue
    remaining_brown = brown_shirts - third_brown
    total_remaining = remaining_blue + remaining_brown
    result = total_remaining
    return result

print(solution())