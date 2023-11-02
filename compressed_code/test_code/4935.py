def solution():
    
    total_pigeons = 70
    black_pigeons = total_pigeons / 2
    black_male_pigeons = black_pigeons * 0.2
    black_female_pigeons = black_pigeons - black_male_pigeons
    difference = black_female_pigeons - black_male_pigeons
    result = difference
    return result

print(solution())