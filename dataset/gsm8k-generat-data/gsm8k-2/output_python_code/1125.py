def solution():
    """Mike is building a bridge out of LEGO blocks. To be successful he needs at least 40 bricks of type A, and half that many of type B. In total, he needs to use 150 bricks. How many bricks of other types than mentioned is he going to use?"""
    type_a_bricks = 40
    type_b_bricks = type_a_bricks / 2
    total_bricks_needed = 150
    bricks_of_other_types = total_bricks_needed - type_a_bricks - type_b_bricks
    result = bricks_of_other_types
    return result

print(solution())