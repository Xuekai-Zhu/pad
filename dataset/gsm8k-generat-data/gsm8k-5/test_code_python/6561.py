def solution():
    total_rope = 50  # Bob buys 50 feet of rope
    small_piece = total_rope / 5  # Bob uses a 5th of the rope for a small piece of art
    remaining_rope = total_rope - small_piece  # Bob has the remaining rope
    half_rope = remaining_rope / 2  # Bob gives half of the remaining rope to his friend
    sections = half_rope // 2  # Bob cuts the rope into 2-foot sections and counts how many he gets

    result = sections
    return result

print(solution())