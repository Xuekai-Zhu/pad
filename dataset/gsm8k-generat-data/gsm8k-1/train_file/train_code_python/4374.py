def solution():
    """A quarterback throws 50 passes in one game. He throws twice as many passes to the right of the field than he does to the left of the field. He throws 2 more passes to the center of the field than he did to the left. How many passes did he throw to the left side of the field?"""
    total_passes = 50
    passes_to_left = x
    passes_to_right = 2 * passes_to_left
    passes_to_center = passes_to_left + 2
    total_passes = passes_to_left + passes_to_right + passes_to_center
    passes_to_left = (total_passes - passes_to_center) / 3
    result = passes_to_left
    return result

print(solution())