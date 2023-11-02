def solution():
    
    total_characters = 60
    half_a = total_characters // 2
    half_c = half_a // 2
    half_d_e = total_characters - half_a - half_c
    d = 2 * (half_d_e // 3)
    result = d
    return result

print(solution())