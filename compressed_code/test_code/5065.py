def solution():
    
    total_rope = 50
    art_rope = total_rope / 5
    remaining_rope = total_rope - art_rope
    friend_rope = remaining_rope / 2
    cutting_rope = friend_rope
    sections = cutting_rope / 2
    result = sections
    return result

print(solution())