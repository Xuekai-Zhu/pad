def solution():
    
    colored_pencils = 14
    black_pencils = 35
    total_pencils = colored_pencils + black_pencils
    num_siblings = 3
    pencils_to_share = total_pencils - 10
    pencils_per_sib = pencils_to_share / num_siblings
    result = pencils_per_sib
    return result

print(solution())