def solution():
    total_rope = 20
    share_to_allan = total_rope / 4
    remaining_rope = total_rope - share_to_allan
    share_to_jack = remaining_rope * (2/3)
    left_rope = remaining_rope - share_to_jack
    result = left_rope
    return result

print(solution())