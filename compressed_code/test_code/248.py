def solution():
    
    story_height = 10
    total_height = 6 * story_height
    rope_length = 20
    loss_percentage = 25
    actual_rope_length = rope_length - (rope_length * loss_percentage / 100)
    pieces_of_rope_needed = total_height / actual_rope_length
    result = round(pieces_of_rope_needed)
    return result

print(solution())