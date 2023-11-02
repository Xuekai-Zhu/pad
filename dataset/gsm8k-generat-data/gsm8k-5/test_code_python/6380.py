def solution():
    total_pigeons = 70  # The park has 70 pigeons
    black_pigeons = total_pigeons / 2  # Half of the pigeons are black
    black_male_pigeons = black_pigeons * 0.2  # 20 percent of the black pigeons are male
    black_female_pigeons = black_pigeons - black_male_pigeons  # Calculate the number of black female pigeons

    # Determine how many more black female pigeons there are than black male pigeons
    difference = black_female_pigeons - black_male_pigeons
    result = difference
    return result

print(solution())