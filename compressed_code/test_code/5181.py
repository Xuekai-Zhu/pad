def solution():
    
    total_sheep = 400
    sheep_to_sister = total_sheep // 4
    remaining_sheep = total_sheep - sheep_to_sister
    sheep_to_brother = remaining_sheep // 2
    sheep_with_mary = remaining_sheep - sheep_to_brother
    result = sheep_with_mary
    return result

print(solution())