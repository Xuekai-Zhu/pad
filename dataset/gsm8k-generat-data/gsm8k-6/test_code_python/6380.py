def solution():
    # Calculate the number of black pigeons
    black_pigeons = 70 / 2
    # Calculate the number of black male pigeons
    black_male_pigeons = black_pigeons * 0.2
    # Calculate the number of black female pigeons
    black_female_pigeons = black_pigeons - black_male_pigeons
    # Calculate the difference between the number of black female pigeons and black male pigeons
    difference = black_female_pigeons - black_male_pigeons
    result = difference
    return result

print(solution())