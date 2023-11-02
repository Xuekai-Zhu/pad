def solution():
    
    orlan_rope = 20
    allan_rope = orlan_rope / 4
    remaining_rope_1 = orlan_rope - allan_rope
    jack_rope = (2/3) * remaining_rope_1
    remaining_rope_2 = remaining_rope_1 - jack_rope
    result = remaining_rope_2
    return result

print(solution())