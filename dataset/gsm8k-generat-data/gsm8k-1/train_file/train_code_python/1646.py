def solution():
    """Ellie and Sarah got lost in the house of mirrors. They saw their reflections in the tall mirrors 3 times each and in the wide mirrors 5 times each. Sarah saw her reflection 10 times in the tall mirrors and 5 times in the wide mirrors, while Ellie saw her reflection 6 times in the tall mirrors and 3 times in the wide mirrors. How many times did they see their reflections in total?"""
    tall_mirror_reflections_sarah = 10 * 3
    wide_mirror_reflections_sarah = 5 * 5
    tall_mirror_reflections_ellie = 6 * 3
    wide_mirror_reflections_ellie = 3 * 5
    total_reflections = tall_mirror_reflections_sarah + wide_mirror_reflections_sarah + tall_mirror_reflections_ellie + wide_mirror_reflections_ellie
    result = total_reflections
    return result

print(solution())