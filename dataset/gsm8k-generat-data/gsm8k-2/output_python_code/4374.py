def solution():
    """A quarterback throws 50 passes in one game. He throws twice as many passes to the right of the field than he does to the left of the field. He throws 2 more passes to the center of the field than he did to the left. How many passes did he throw to the left side of the field?"""
    total_passes = 50
    right_passes = 2 * left_passes
    center_passes = left_passes + 2
    all_passes = left_passes + right_passes + center_passes
    left_passes = (total_passes - center_passes) / 3
    result = left_passes
    return result

print(solution())