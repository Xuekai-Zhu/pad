def solution():
    # Calculate number of black pigeons
    black_pigeons = 70 / 2
    
    # Calculate number of black male pigeons
    black_male = black_pigeons * 0.2
    
    # Calculate number of black female pigeons
    black_female = black_pigeons - black_male
    
    # Calculate difference between black female and black male pigeons
    difference = black_female - black_male
    
    result = difference
    return result

print(solution())