def solution():
    total_rope_length = 50
    portion_used_for_art = total_rope_length / 5
    remaining_rope_length = total_rope_length - portion_used_for_art
    remaining_rope_length /= 2 # divide by 2 to give half to friend
    num_sections = remaining_rope_length / 2  # cut into 2-foot sections
    result = num_sections
    return result

print(solution())