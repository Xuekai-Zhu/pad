def solution():
    num_pigeons = 70
    black_pigeons = num_pigeons / 2
    black_male_pigeons = black_pigeons * 0.2
    black_female_pigeons = black_pigeons - black_male_pigeons
    
    # Calculate the difference between the number of black female and black male pigeons
    difference = black_female_pigeons - black_male_pigeons
    
    result = difference
    return result

print(solution())